"""FastAPI proxy application for Lixinger API."""

from typing import Any

import json

import httpx
from fake_useragent import UserAgent
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

from .cache_manager import CacheManager
from .config import settings
from .rate_limiter import RateLimiter

# Initialize FastAPI app
app = FastAPI(
    title="Lixinger API Proxy",
    description="Proxy service for Lixinger API with TTL cache and rate limiting",
    version="0.1.0",
)

# Initialize cache manager and rate limiter
cache_manager = CacheManager()
rate_limiter = RateLimiter()

# Initialize user agent
ua = UserAgent()


@app.api_route("/api/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_request(path: str, request: Request) -> Response:
    """Proxy all requests to Lixinger API with caching for GET and POST.

    Args:
        path: API endpoint path
        request: FastAPI request object

    Returns:
        JSON response from upstream API or cache
    """
    method = request.method.upper()

    # Prepare request data based on method
    query_params = dict(request.query_params)
    body_text: str | None = None
    json_body: dict[str, Any] | None = None

    if method == "GET":
        # GET: token in query params
        if "token" not in query_params:
            query_params["token"] = settings.lxr_api_token
    else:
        # POST/PUT/DELETE/PATCH: token in body
        try:
            json_body = await request.json()
            if isinstance(json_body, dict) and "token" not in json_body:
                json_body["token"] = settings.lxr_api_token
            body_text = json.dumps(json_body, sort_keys=True, ensure_ascii=False)
        except Exception:
            body_text = "{}"

    # Check cache for GET and POST
    if method in {"GET", "POST"}:
        cached_data = cache_manager.get(method, path, query_params, body_text)
        if cached_data is not None:
            return JSONResponse(
                content=cached_data,
                headers={"X-Cache": "HIT"},
            )

    # Apply rate limiting (wait if needed)
    try:
        wait_time = await rate_limiter.wait_if_needed()
        if wait_time > 0:
            print(f"Rate limit: waited {wait_time:.2f}s before forwarding request")
    except ValueError as e:
        # Rate limit exceeded max wait time
        return JSONResponse(
            status_code=429,
            content={"error": str(e)},
            headers={"Retry-After": str(settings.rate_limit_max_wait_seconds)},
        )

    # Forward request to upstream API
    upstream_url = f"{settings.upstream_api_base}/{path}"
    headers = {
        "User-Agent": ua.chrome,
    }

    headers["Content-Type"] = request.headers.get("Content-Type", "application/json")

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            if method == "GET":
                response = await client.get(
                    upstream_url,
                    params=query_params,
                    headers=headers,
                )
            else:
                response = await client.request(
                    method=method,
                    url=upstream_url,
                    params=query_params,
                    headers=headers,
                    json=json_body,
                )

            response.raise_for_status()

            # Parse JSON response
            try:
                response_data = response.json()

                # Cache successful responses for GET and POST
                if method in {"GET", "POST"} and response.status_code < 400:
                    cache_manager.set(
                        method, path, query_params, response_data, body_text
                    )

                return JSONResponse(
                    content=response_data,
                    status_code=response.status_code,
                    headers={"X-Cache": "MISS"} if method in {"GET", "POST"} else {},
                )
            except Exception:
                # Return raw response if not JSON
                return Response(
                    content=response.content,
                    status_code=response.status_code,
                    media_type=response.headers.get("Content-Type", "text/plain"),
                )

        except httpx.HTTPStatusError as e:
            return JSONResponse(
                status_code=e.response.status_code,
                content={"error": f"Upstream API error: {e.response.text}"},
            )
        except httpx.RequestError as e:
            return JSONResponse(
                status_code=502,
                content={"error": f"Failed to connect to upstream API: {str(e)}"},
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"error": f"Internal server error: {str(e)}"},
            )


@app.get("/")
async def root() -> dict[str, Any]:
    """Root endpoint with service information."""
    return {
        "service": "Lixinger API Proxy",
        "version": "0.1.0",
        "author": "wisdomvalley",
        "endpoints": {
            "proxy": "/api/{path}",
        },
        "cache": {
            "ttl_seconds": settings.cache_ttl_seconds,
            "max_size": settings.cache_max_size,
            "current_size": len(cache_manager.cache),
            "cache_dir": settings.cache_dir,
        },
        "rate_limit": {
            "window_seconds": settings.rate_limit_window_seconds,
            "max_requests": settings.rate_limit_max_requests,
            "current_requests": len(rate_limiter.request_timestamps),
        },
    }


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
