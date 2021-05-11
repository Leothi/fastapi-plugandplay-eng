from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException


class APIException(Exception):
    """Base class for personalized API Exceptions.

    :param Exception: Python Exception class.
    """

    def __init__(self, status: int, message: str):
        self.status_code = status
        self.message = message


# Exception creation/replacement
class ExceptionHandler:

    def __init__(self, app: FastAPI):
        app.exception_handler(Exception)(self.exception_handler)
        app.exception_handler(HTTPException)(self.http_excep)
        app.exception_handler(APIException)(self.camara_exception_handler)
        app.exception_handler(RequestValidationError)(
            self.validation_exception_handler)

    @staticmethod
    async def exception_handler(request: Request, exception: Exception):
        return JSONResponse(
            status_code=500, content={
                "status": 500,
                "message": 'Internal Server Error'
            }
        )

    @staticmethod
    async def http_excep(request: Request, exception: HTTPException):
        message = {404: "Not Found",
                   500: "Internal Server Error'",
                   400: "Bad Request"}
        return JSONResponse(
            status_code=exception.status_code,
            content={
                "status": exception.status_code,
                "message": message[exception.status_code]
            }
        )

    @staticmethod
    async def camara_exception_handler(request: Request, exception: APIException):
        return JSONResponse(
            status_code=exception.status_code,
            content={
                "status": exception.status_code,
                "message": exception.message
            }
        )

    @staticmethod
    async def validation_exception_handler(request: Request, exception: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={
                "status": 422,
                "message": "Invalid request parameters.",
                "details": str(exception)
            }
        )
