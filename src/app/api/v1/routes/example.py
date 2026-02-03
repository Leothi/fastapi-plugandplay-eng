from fastapi import APIRouter, Query

from app.schemas.example import ExampleIn, ExampleOut
from app.services.example import string_upper

router = APIRouter()


@router.get("/upper", response_model=ExampleOut, summary="Uppercase a string")
async def get_upper(text: str = Query(..., min_length=1, examples=["hello"])) -> ExampleOut:
    return ExampleOut(original=text, upper=string_upper(text))


@router.post("/upper", response_model=ExampleOut, summary="Uppercase a string")
async def post_upper(body: ExampleIn) -> ExampleOut:
    return ExampleOut(original=body.text, upper=string_upper(body.text))
