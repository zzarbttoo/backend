# controllers/items.py
from fastapi import APIRouter, Response, status

router = APIRouter(prefix="/api")

from datetime import datetime
from app.models.HttpDtos import Home, Page, HomeResponseWithPage, WholeHomeResponseList, HomeResponse

@router.get("/home/", response_model=WholeHomeResponseList, description="""주택 전체 목록 """)
async def read_items(response:Response):

    homes_data = [
        [1, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
        [2, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
        [3, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
        [4, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
    ]

    response.status_code = status.HTTP_200_OK 
    return WholeHomeResponseList(homeList=[Home(*data) for data in homes_data])

@router.get("/home/{home_seq}", description="""주택 세부 조회 """)
async def read_item(home_seq: int):
    return HomeResponse([1, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False])
    


@router.get("/home/page", response_model=HomeResponseWithPage, description="""주택 페이지 목록""")
async def read_item_as_page(response:Response, page:Page):
    # 가상의 데이터라고 가정합니다.
    page = Page(total=10, current=1)
    homes_data = [
        [1, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
        [2, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
        [3, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
        [4, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
    ]
    response.status_code = status.HTTP_200_OK
    response_data = Home( homeList=[Home(*data) for data in homes_data])
    
    return  response_data
