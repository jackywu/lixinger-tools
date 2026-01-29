"""Rate limiter using sliding window algorithm."""

import time
from threading import Lock

from .config import settings


class RateLimiter:
    """Global rate limiter using sliding window algorithm."""

    def __init__(self):
        """Initialize the rate limiter."""
        self.window_seconds = settings.rate_limit_window_seconds
        self.max_requests = settings.rate_limit_max_requests
        self.max_wait_seconds = settings.rate_limit_max_wait_seconds
        
        # Store timestamps of requests in the current window
        self.request_timestamps: list[float] = []
        self.lock = Lock()

    def _clean_old_timestamps(self, current_time: float) -> None:
        """Remove timestamps outside the current window.
        
        Args:
            current_time: Current timestamp
        """
        cutoff_time = current_time - self.window_seconds
        self.request_timestamps = [
            ts for ts in self.request_timestamps if ts > cutoff_time
        ]

    def get_wait_time(self) -> float:
        """Calculate how long to wait before making the next request.
        
        Returns:
            Wait time in seconds (0 if request can proceed immediately)
            
        Raises:
            ValueError: If wait time exceeds max_wait_seconds
        """
        with self.lock:
            current_time = time.time()
            self._clean_old_timestamps(current_time)
            
            # Check if we're within the limit
            if len(self.request_timestamps) < self.max_requests:
                return 0.0
            
            # Calculate wait time: time until oldest request exits the window
            oldest_timestamp = self.request_timestamps[0]
            wait_time = (oldest_timestamp + self.window_seconds) - current_time
            
            # Check if wait time exceeds maximum allowed
            if wait_time > self.max_wait_seconds:
                raise ValueError(
                    f"Rate limit exceeded. Would need to wait {wait_time:.1f}s "
                    f"(max allowed: {self.max_wait_seconds}s)"
                )
            
            return max(0.0, wait_time)

    def record_request(self) -> None:
        """Record a new request timestamp."""
        with self.lock:
            current_time = time.time()
            self._clean_old_timestamps(current_time)
            self.request_timestamps.append(current_time)

    async def wait_if_needed(self) -> float:
        """Wait if rate limit is reached, then record the request.
        
        Returns:
            Time waited in seconds
            
        Raises:
            ValueError: If wait time exceeds max_wait_seconds
        """
        import asyncio
        
        wait_time = self.get_wait_time()
        
        if wait_time > 0:
            await asyncio.sleep(wait_time)
        
        self.record_request()
        return wait_time
