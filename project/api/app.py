import sys

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from api import __version__
from api.routes import example
from api.schemas import DEFAULT_RESPONSES_JSON
from api.modules.default.middleware import Middleware
from api.exceptions import ExceptionHandler
from api.settings import envs


def get_app() -> FastAPI:
    # Logger configuration
    logger.configure(
        handlers=[
            {
                "sink": sys.stdout,
                "level": envs.LOG_LEVEL,
                "format": envs.LOGURU_FORMAT
            }
        ]
    )

    # Levels criation
    logger.level('REQUEST RECEIVED', no=37, color="<yellow>")
    logger.level('REQUEST DONE', no=38, color="<yellow>")
    logger.level('LOG ROUTE', no=39, color="<light-green>")

    async def startup_event():
        global rm_model
        logger.info("Starting API")

    async def shutdown_event():
        logger.info("API shutdown")

    if envs.RUNNING_ENV == 'dev':
        # Logger output file
        logger.add("./logs/test.log", level=0,
                   format=envs.LOGURU_FORMAT, rotation='500 MB')
        logger.add("./logs/test_error.log", level=40,
                   format=envs.LOGURU_FORMAT, rotation='500 MB')

    # API Instance
    app = FastAPI(title='Plug and Play API',
                  description="Project plug and play architecture.",
                  version=__version__,
                  root_path=envs.FASTAPI_ROOT_PATH,
                  on_startup=[startup_event],
                  on_shutdown=[shutdown_event],
                  )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Router
    app.include_router(
        example.router, prefix='/example', tags=['Route example'],
        responses={**DEFAULT_RESPONSES_JSON})

    # API Modules
    Middleware(app)
    ExceptionHandler(app)

    return app
