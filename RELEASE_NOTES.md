# Release Notes — FastAPI Plug and Play Modernization

Date: 2026-02-03
Branch: chore/modernize-template

## Highlights
- Migrated to a modern `src/` layout with a new app factory, routers, schemas, services, and tests.
- Upgraded to Pydantic v2 with `pydantic-settings` for configuration.
- Added request ID + timing middleware.
- Modernized Docker/Compose and documentation.
- Added linting, formatting, typing, tests, coverage, pre-commit, and CI with `uv`.

## What’s New
- New app package in `src/app/` and tests in `tests/`.
- CI pipeline in `.github/workflows/ci.yml`.
- Tooling configured via `pyproject.toml` (Ruff, Mypy, Pytest, Coverage).

## Removed
- Legacy `project/` layout and `.flake8` (replaced by Ruff).

## Notes
- Ruff has pending import-order fixes in:
  - `src/app/core/middleware.py`
  - `tests/test_example.py`
  - `tests/test_health.py`