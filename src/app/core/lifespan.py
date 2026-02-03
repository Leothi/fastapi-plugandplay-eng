from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.mongo import close_mongo, connect_mongo


@asynccontextmanager
async def lifespan(_: FastAPI):
    await connect_mongo()
    yield
    await close_mongo()
