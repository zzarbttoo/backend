# controllers/items.py
from fastapi import APIRouter, Response, status

router = APIRouter()

from datetime import datetime
from app.models.HttpDtos import Home, Page, HomeResponseWithPage, WholeHomeResponseList

@router.get("/home/", response_model=WholeHomeResponseList, description="""주택 전체 목록 """)
async def read_items(response:Response):

    homes_data = [
        [1, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간"], 
    ]

    response.status_code = status.HTTP_200_OK 
    return WholeHomeResponseList(homeList=[Home(*data) for data in homes_data])

@router.get("/home/{item_id}", description="""주택 세부 조회 """)
async def read_item(item_id: int):
    return {"message": f"Read item with ID {item_id}"}


@router.get("/home/page", response_model=HomeResponseWithPage, description="""주택 페이지 목록""")
async def read_item_as_page(response:Response, page:Page):
    # 가상의 데이터라고 가정합니다.
    page = Page(total=10, current=1)
    homes_data = [
        [1, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간"], 
    ]

    response.status_code = status.HTTP_200_OK
    response_data = HomeResponseWithPage(page=page, homeList=[Home(*data) for data in homes_data])
    
    return  response_data

# @router.post("/items/")
# async def create_item():
#     return {"message": "Create a new item"}


@router.post("/items/temp")
async def create_item_with_body(req:Home):
    print(req)

