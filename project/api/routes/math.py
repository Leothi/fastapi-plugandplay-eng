from fastapi import APIRouter, Query
from loguru import logger

from api.schemas.example import GetExampleResponse, PostExampleResponse, PostExampleInput
from api.modules import math as module_math

router = APIRouter()


@router.get('/get', summary="Summary 2 - Sum of two numbers")
def router_post(x: int = Query(..., lt=10), y: int = Query(...,)) -> dict:
    "Example of how to sum two numbers"
    return {"example_out": module_math.sum_two_numbers(x, y)}
