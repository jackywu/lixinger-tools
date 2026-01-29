# Lixinger API Proxy

A FastAPI-based proxy service for the Lixinger API with TTL caching and intelligent rate limiting.

## Features

- **TTL Caching**: Responses are cached for 10 hours (configurable) with automatic expiration
- **Persistent Cache**: Cache stored in JSON files (per API endpoint) for data persistence across restarts
- **Rate Limiting**: Global sliding window rate limiter (default: 10 requests per minute)
- **Smart Waiting**: Automatically waits during rate limit windows (up to 10 minutes)
- **Browser Simulation**: Uses Chrome User-Agent for upstream requests
- **GET Request Caching**: Only GET requests are cached; POST/PUT/DELETE/PATCH are forwarded directly

## Installation

```bash
# Install dependencies using uv
uv sync

# Or using pip
pip install -e .
```

## Configuration

Create a `.env` file in the project root:

```env
LXR_API_TOKEN=your_lixinger_api_token_here
CACHE_TTL_SECONDS=36000
CACHE_MAX_SIZE=5000
RATE_LIMIT_WINDOW_SECONDS=60
RATE_LIMIT_MAX_REQUESTS=10
RATE_LIMIT_MAX_WAIT_SECONDS=600
```

### Configuration Options

- `LXR_API_TOKEN` (required): Your Lixinger API token
- `CACHE_TTL_SECONDS` (default: 36000): Cache time-to-live in seconds (10 hours)
- `CACHE_MAX_SIZE` (default: 5000): Maximum number of cached items
- `RATE_LIMIT_WINDOW_SECONDS` (default: 60): Rate limit time window in seconds
- `RATE_LIMIT_MAX_REQUESTS` (default: 10): Maximum requests per time window
- `RATE_LIMIT_MAX_WAIT_SECONDS` (default: 600): Maximum wait time when rate limited (10 minutes)

## Usage

### Start the server

```bash
# Using Python module
python -m lxrtools.main

# Or using uv
uv run python -m lxrtools.main
```

The server will start on `http://localhost:8000`

### API Endpoints

#### Proxy Endpoint

All Lixinger API calls should be made to:

```
http://localhost:8000/api/{path}
```

For example:
- Original: `https://open.lixinger.com/api/a/stock`
- Proxied: `http://localhost:8000/api/a/stock`

#### Service Information

```bash
# Get service info and current status
curl http://localhost:8000/

# Health check
curl http://localhost:8000/health
```

### Example Usage

```bash
# Get stock data (will be cached)
curl "http://localhost:8000/api/a/stock?stockCode=600000"

# Second request will return cached data (X-Cache: HIT header)
curl -v "http://localhost:8000/api/a/stock?stockCode=600000"
```

### Response Headers

- `X-Cache: HIT` - Response served from cache
- `X-Cache: MISS` - Response fetched from upstream API

## Cache Storage

Cache files are stored in:
- **Linux**: `~/.cache/lxrtools/wisdomvalley/`
- **macOS**: `~/Library/Caches/lxrtools/wisdomvalley/`
- **Windows**: `C:\Users\<username>\AppData\Local\wisdomvalley\lxrtools\Cache\`

Each cached API response is stored in a separate JSON file for better organization and readability.

## Rate Limiting

The service implements a global sliding window rate limiter:

1. Tracks requests in a 60-second window
2. Limits to 10 requests per window
3. When limit is reached, the service waits automatically
4. Maximum wait time is 10 minutes (returns 429 error if exceeded)

## Architecture

```
src/lxrtools/
├── __init__.py          # Package initialization
├── main.py              # Application entry point
├── config.py            # Pydantic settings configuration
├── cache_manager.py     # TTL cache with JSON persistence
├── rate_limiter.py      # Sliding window rate limiter
└── proxy.py             # FastAPI application and routes
```

## Development

```bash
# Install dev dependencies
uv sync

# Run with auto-reload
uvicorn lxrtools.proxy:app --reload

# Type checking
mypy src/lxrtools

# Linting
ruff check src/lxrtools
```

## License

MIT License

## Author

wisdomvalley
