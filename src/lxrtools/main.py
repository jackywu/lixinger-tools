"""Main entry point for Lixinger API Proxy."""

import uvicorn

from .proxy import app


def main():
    """Start the FastAPI application."""
    print("Starting Lixinger API Proxy...")
    print("Cache and rate limiting enabled")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )


if __name__ == "__main__":
    main()
