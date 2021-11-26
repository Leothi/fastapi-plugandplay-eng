from pydantic import Field, BaseModel

from api.schemas import SuccessResponse


class GetExampleResponse(SuccessResponse):
    """Response model to /get"""
    example_out: str = Field(...,
                             description="Upper case string.", example="STRING")
    get_message: str = Field("GET request example.",
                             description="Example message.",
                             example="GET request example.")


class PostExampleInput(BaseModel):
    """ Post input base model """
    string: str = Field(..., description="String to be transformed to upper case.", example="string")


class PostExampleResponse(SuccessResponse):
    """Response model to /post"""
    example_out: str = Field(...,
                             description="Upper case string", example="STRING")
    post_message: str = Field("POST request example.",
                              description="Message example.",
                              example="POST request example.")
