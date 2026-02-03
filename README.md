# FastAPI Plug and Play (Modernized)
A modern, batteries-included FastAPI template with a clean `src/` layout, Pydantic v2 settings, typed services, and CI-ready tooling.

## Quick Start
1. Install dependencies

```bash
uv sync --dev
```

2. Run the API

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

3. Open docs

- Swagger UI: `http://localhost:8080/docs`
- OpenAPI: `http://localhost:8080/api/v1/openapi.json`

## Tooling
- Lint/format

```bash
uv run ruff check .
uv run ruff format .
```

- Type check

```bash
uv run mypy src
```

- Tests

```bash
uv run pytest
```

## Docker
Build and run:

```bash
docker build -t fastapi-plugandplay .
docker run -p 8080:8080 --env-file .env fastapi-plugandplay
```

## Environment
Copy `.env.example` to `.env` and adjust values as needed.

## Dependency Locking
To pin deterministic builds, generate a lockfile:

```bash
uv lock
```

Commit `uv.lock` for reproducible deployments.