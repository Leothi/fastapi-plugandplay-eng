from __future__ import annotations

import logging

from pymongo import AsyncMongoClient

from app.core.config import settings

logger = logging.getLogger("app.db.mongo")

_client: AsyncMongoClient | None = None


async def connect_mongo() -> None:
    global _client
    if not settings.mongo_dsn:
        logger.info("MongoDB DSN not configured; skipping connection")
        return
    _client = AsyncMongoClient(settings.mongo_dsn)
    logger.info("MongoDB client initialized")


async def close_mongo() -> None:
    global _client
    if _client is not None:
        _client.close()
        _client = None
        logger.info("MongoDB client closed")


def get_database():
    if _client is None:
        raise RuntimeError("MongoDB client is not initialized")
    return _client[settings.mongo_db]
