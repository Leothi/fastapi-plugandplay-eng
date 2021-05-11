from pydantic import BaseModel, Field


class SuccessResponse(BaseModel):
    """Base model for Success Response"""
    message = "Processed with success."
    message: str = Field(message,
                         example=message)


class ErrorResponse(BaseModel):
    """Base model for Error Response"""
    status: int = Field(..., description="Message code")
    message: str = Field(..., description="Message description")
    details: str = Field(None, description="Message details")


DEFAULT_RESPONSES = [
    ErrorResponse(status=422, message="Invalid request body",
                  details="1 validation error for Request..."),
    ErrorResponse(status=500, message="Internal Error!"),
    ErrorResponse(status=404, message="Not found"),
    ErrorResponse(status=400, message="Bad Request"),
]


def parse_openapi(responses: list = list()) -> dict:
    responses.extend(DEFAULT_RESPONSES)
    return {example.status: {"content": {"application/json": {"example": example.dict()}}, "model": ErrorResponse}
            for example in responses}


DEFAULT_RESPONSES_JSON = parse_openapi()
