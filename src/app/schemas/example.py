from pydantic import BaseModel, Field


class ExampleIn(BaseModel):
    text: str = Field(..., min_length=1, examples=["hello"])


class ExampleOut(BaseModel):
    original: str
    upper: str
