# Modernization Changes

Date: 2026-02-03
Branch: chore/modernize-template

## Summary
- Migrated to a modern `src/` layout with a new app factory, settings, routers, schemas, services, and tests.
- Switched to Pydantic v2 and `pydantic-settings` for configuration.
- Added middleware for request IDs and request timing.
- Added MongoDB async client scaffold (PyMongo async API) with lifespan hooks.
- Modernized Docker, Compose, and documentation.
- Added linting, formatting, typing, tests, coverage, and pre-commit tooling.
- Added CI workflow using `uv`.

## New Structure
- `src/app/` (new application package)
- `tests/` (pytest tests)
- `.github/workflows/ci.yml`

## New/Updated Files
- `pyproject.toml` (PEP 621, dependency groups, Ruff, Mypy, Pytest, Coverage)
- `.python-version`
- `.env.example`
- `.editorconfig`
- `.pre-commit-config.yaml`
- `Dockerfile`
- `docker-compose.yml`
- `docker-compose-dev.yml`
- `README.md`

### App code
- `src/app/__init__.py`
- `src/app/__main__.py`
- `src/app/main.py`
- `src/app/core/config.py`
- `src/app/core/logging.py`
- `src/app/core/lifespan.py`
- `src/app/core/middleware.py`
- `src/app/api/v1/router.py`
- `src/app/api/v1/routes/health.py`
- `src/app/api/v1/routes/example.py`
- `src/app/schemas/health.py`
- `src/app/schemas/example.py`
- `src/app/services/example.py`
- `src/app/db/mongo.py`

### Tests
- `tests/test_health.py`
- `tests/test_example.py`

## Removed
- `project/` (legacy layout)
- `.flake8` (replaced by Ruff)

## Dependency Updates (high level)
- FastAPI, Uvicorn, Pydantic v2, Pydantic Settings, PyMongo upgraded.
- Tooling: Ruff, Mypy, Pytest, Coverage, Pre-commit added/updated.

## Environment & Tooling
- Uses `uv` for dependency management and lockfiles.
- CI workflow runs lint, format check, type check, and tests.

## Tests Run
- `uv run pytest` (3 passed)

## Notes
- Ruff lint still has import-order findings pending auto-fix in:
  - `src/app/core/middleware.py`
  - `tests/test_example.py`
  - `tests/test_health.py`