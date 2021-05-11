from fastapi import APIRouter, Query
from loguru import logger

from api.models.example import GetExampleResponse, PostExampleResponse, PostExampleInput
from api.modules import example as modulo_example

router = APIRouter()


@router.get('/get', response_model=GetExampleResponse, summary="Summary 1 - String to upper case.")
def router_get(string: str = Query(..., 
                                   description="Input string.", 
                                   example="string")) -> dict:
    """GET route example. Returns input string in upper case."""

    logger.log('LOG ROUTE', "Calling /get route")
    return {"example_out": modulo_example.string_upper(string)}


@router.post('/post', response_model=PostExampleResponse,
             summary="Summary 2 - String upper case.")
def router_post(body: PostExampleInput) -> dict:
    """POST route example. Returns input string in upper case."""

    logger.log('LOG ROUTE', "Calling /post route")
    return {"example_out": modulo_example.string_upper(body.dict()['string'])}
