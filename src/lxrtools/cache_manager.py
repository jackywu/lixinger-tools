"""TTL cache manager with JSON persistence."""

import hashlib
import json
import time
from pathlib import Path
from threading import Lock
from typing import Any
from urllib.parse import urlencode

from .config import settings


class CacheManager:
    """Manages TTL-based caching with JSON file persistence per API endpoint."""

    def __init__(self) -> None:
        """Initialize the cache manager."""
        self.cache_dir = Path(settings.cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.ttl_seconds = settings.cache_ttl_seconds
        self.max_size = settings.cache_max_size
        self.lock = Lock()

        # In-memory cache: {cache_key: {"data": response_data, "expires_at": timestamp}}
        self.cache: dict[str, dict[str, Any]] = {}

        # Load existing cache from disk
        self._load_all_from_disk()

    def _generate_cache_key(
        self,
        method: str,
        path: str,
        query_params: dict[str, Any],
        body_text: str | None,
    ) -> str:
        """Generate cache key from method, URL path, sorted query parameters, and body.

        Args:
            path: API endpoint path (e.g., "/a/stock")
            query_params: Query parameters dictionary

        Returns:
            Cache key as a string (path + sorted query params)
        """
        key_parts = [method.upper(), path]
        if query_params:
            sorted_params = urlencode(sorted(query_params.items()))
            key_parts.append(f"?{sorted_params}")
        if body_text:
            key_parts.append(f"|body:{body_text}")
        return "".join(key_parts)

    def _get_cache_file_path(self, cache_key: str) -> Path:
        """Get the file path for a cache key.

        Args:
            cache_key: The cache key (path + query params)

        Returns:
            Path to the JSON cache file
        """
        # Use hash of cache key as filename to avoid filesystem issues
        key_hash = hashlib.md5(cache_key.encode()).hexdigest()
        return self.cache_dir / f"{key_hash}.json"

    def get(
        self,
        method: str,
        path: str,
        query_params: dict[str, Any],
        body_text: str | None = None,
    ) -> dict[str, Any] | None:
        """Get cached response if exists and not expired.

        Args:
            path: API endpoint path
            query_params: Query parameters

        Returns:
            Cached response data or None if not found/expired
        """
        cache_key = self._generate_cache_key(method, path, query_params, body_text)

        with self.lock:
            if cache_key in self.cache:
                entry = self.cache[cache_key]
                if time.time() < entry["expires_at"]:
                    return entry["data"]
                else:
                    # Expired, remove from cache
                    del self.cache[cache_key]
                    self._delete_cache_file(cache_key)

        return None

    def set(
        self,
        method: str,
        path: str,
        query_params: dict[str, Any],
        data: dict[str, Any],
        body_text: str | None = None,
    ) -> None:
        """Store response data in cache with TTL.

        Args:
            path: API endpoint path
            query_params: Query parameters
            data: Response data to cache
        """
        cache_key = self._generate_cache_key(method, path, query_params, body_text)
        expires_at = time.time() + self.ttl_seconds

        with self.lock:
            # Check if we need to evict old entries
            if len(self.cache) >= self.max_size and cache_key not in self.cache:
                self._evict_oldest()

            self.cache[cache_key] = {
                "data": data,
                "expires_at": expires_at,
            }

            # Persist to disk
            self._save_to_disk(cache_key)

    def _evict_oldest(self) -> None:
        """Evict the oldest cache entry (by expiration time)."""
        if not self.cache:
            return

        # Find entry with earliest expiration
        oldest_key = min(self.cache.keys(), key=lambda k: self.cache[k]["expires_at"])
        del self.cache[oldest_key]
        self._delete_cache_file(oldest_key)

    def _save_to_disk(self, cache_key: str) -> None:
        """Save a single cache entry to disk.

        Args:
            cache_key: The cache key to save
        """
        if cache_key not in self.cache:
            return

        file_path = self._get_cache_file_path(cache_key)
        entry = self.cache[cache_key]

        cache_data = {
            "cache_key": cache_key,
            "data": entry["data"],
            "expires_at": entry["expires_at"],
        }

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(cache_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Failed to save cache to {file_path}: {e}")

    def _load_all_from_disk(self) -> None:
        """Load all cache entries from disk on startup."""
        if not self.cache_dir.exists():
            return

        current_time = time.time()

        for cache_file in self.cache_dir.glob("*.json"):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    cache_data = json.load(f)

                cache_key = cache_data["cache_key"]
                expires_at = cache_data["expires_at"]

                # Skip expired entries
                if current_time >= expires_at:
                    cache_file.unlink(missing_ok=True)
                    continue

                self.cache[cache_key] = {
                    "data": cache_data["data"],
                    "expires_at": expires_at,
                }

            except Exception as e:
                print(f"Failed to load cache from {cache_file}: {e}")
                # Delete corrupted cache file
                cache_file.unlink(missing_ok=True)

    def _delete_cache_file(self, cache_key: str) -> None:
        """Delete cache file from disk.

        Args:
            cache_key: The cache key to delete
        """
        file_path = self._get_cache_file_path(cache_key)
        file_path.unlink(missing_ok=True)

    def clear_expired(self) -> int:
        """Clear all expired cache entries.

        Returns:
            Number of entries cleared
        """
        current_time = time.time()
        expired_keys = []

        with self.lock:
            for key, entry in self.cache.items():
                if current_time >= entry["expires_at"]:
                    expired_keys.append(key)

            for key in expired_keys:
                del self.cache[key]
                self._delete_cache_file(key)

        return len(expired_keys)
