from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["items"])


@router.get('/items/')
def list_item():
    return [
        "Item A",
        "Item B",
    ]


@router.get('/latest/')
def latest_item():
    return {'item': {'id': "0", "name": "latest"}}


@router.get('/{item_id}/')
def get_item(item_id: Annotated[int, Path(ge=1, lt=1000)]):
    return {"item":
            {"id": item_id}}
