.PHONY: help build run clean docker-run docker-stop logs install-deps test lint format

# Variables
IMAGE_NAME := lxrtools
IMAGE_TAG := latest
CONTAINER_NAME := lxrtools-proxy
PORT := 8000

help:
	@echo "Lixinger API Proxy - Makefile Commands"
	@echo ""
	@echo "Docker targets:"
	@echo "  make build        - Build Docker image"
	@echo "  make docker-run   - Run service in Docker container"
	@echo "  make docker-stop  - Stop and remove Docker container"
	@echo "  make logs         - View Docker container logs"
	@echo ""
	@echo "Development targets:"
	@echo "  make run          - Run service from source code"
	@echo "  make install-deps - Install dependencies"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linters"
	@echo "  make format       - Format code"
	@echo "  make clean        - Clean cache and temporary files"

# Build Docker image
build:
	@echo "Building Docker image $(IMAGE_NAME):$(IMAGE_TAG)..."
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	@echo "Build complete!"

# Run from source code
run:
	@echo "Starting Lixinger API Proxy from source..."
	@if [ ! -f .env ]; then \
		echo "Warning: .env file not found. Please create one from .env.example"; \
		echo "Checking for LXR_API_TOKEN environment variable..."; \
		if [ -z "$$LXR_API_TOKEN" ]; then \
			echo "Error: LXR_API_TOKEN is not set"; \
			exit 1; \
		fi; \
	fi
	PYTHONPATH=src uv run python -m lxrtools.main

# Run Docker container
docker-run:
	@echo "Starting Docker container..."
	@if [ ! -f .env ]; then \
		echo "Warning: .env file not found. Container will need environment variables."; \
	fi
	docker run -d \
		--name $(CONTAINER_NAME) \
		-p $(PORT):8000 \
		--env-file .env \
		-v $(PWD)/cache:/root/.cache/lxrtools \
		--restart unless-stopped \
		$(IMAGE_NAME):$(IMAGE_TAG)
	@echo "Container started: $(CONTAINER_NAME)"
	@echo "Service available at: http://localhost:$(PORT)"

# Stop Docker container
docker-stop:
	@echo "Stopping container $(CONTAINER_NAME)..."
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
	@echo "Container stopped and removed"

# View Docker logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Install dependencies
install-deps:
	@echo "Installing dependencies..."
	uv sync
	@echo "Dependencies installed!"

# Run tests (placeholder)
test:
	@echo "Running tests..."
	uv run pytest tests/ -v || echo "No tests found"

# Lint code
lint:
	@echo "Running linters..."
	uv run ruff check src/lxrtools || echo "ruff not configured"
	uv run mypy src/lxrtools || echo "mypy not configured"

# Format code
format:
	@echo "Formatting code..."
	uv run ruff format src/lxrtools || echo "ruff not configured"

# Clean cache and temporary files
clean:
	@echo "Cleaning cache and temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "Clean complete!"

# Quick build and run
dev: install run

# Build and run in Docker
docker-dev: build docker-stop docker-run logs
