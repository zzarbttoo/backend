# controllers/items.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/items/", description="""items 전체 목록 """)
async def read_items():
    return {"message": "Read all items"}

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"message": f"Read item with ID {item_id}"}

@router.post("/items/")
async def create_item():
    return {"message": "Create a new item"}

from app.models.HttpDtos import Request1

@router.post("/items/temp")
async def create_item_with_body(req:Request1):

    print(req)

