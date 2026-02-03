from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.lifespan import lifespan
from app.core.logging import configure_logging
from app.core.middleware import ProcessTimeMiddleware, RequestIdMiddleware


def create_app() -> FastAPI:
    configure_logging(settings.log_level, json_output=settings.log_json)

    app = FastAPI(
        title=settings.project_name,
        version=settings.version,
        lifespan=lifespan,
        openapi_url=f"{settings.api_v1_prefix}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(RequestIdMiddleware)
    app.add_middleware(ProcessTimeMiddleware)

    app.include_router(api_router, prefix=settings.api_v1_prefix)

    return app


app = create_app()
