# controllers/items.py
from fastapi import APIRouter, Response, status

router = APIRouter(prefix="/api")

from datetime import datetime
from app.models.HttpDtos import Home, Page, HomeResponseWithPage, WholeHomeResponseList, HomeResponse, SortRequest

@router.get("/home/", response_model=WholeHomeResponseList, description="""주택 전체 목록 """)
async def read_items(response:Response, sort_request:SortRequest):
    
    homes_data = [
    [1, "도두일동 2619-1(도두 네오하임)", "340", "40", 30, "84.01", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D",
     True,
     datetime.strptime("2023.10.24", "%Y.%m.%d"), datetime.strptime("2024.10.24", "%Y.%m.%d"), 363],
    [2, "하귀2리 1437(하귀 코아루오션뷰)", "391", "80", 50, "78.9661", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D",
     True,
     datetime.strptime("2023.08.24", "%Y.%m.%d"), datetime.strptime("2023.09.24", "%Y.%m.%d"), 362],
    [3, "도두일동 2619-2(도두 네오하임 주상복합 아파트 2차", "375", "100", 2, "84.34", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D",
     True,
     datetime.strptime("2023.07.24", "%Y.%m.%d"), datetime.strptime("2024.08.22", "%Y.%m.%d"), 361],
    [4, "도두일동 2619-1(도두 네오하임)", "370", "40", 30, "84.01", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D",
     False,
     datetime.strptime("2024.06.24", "%Y.%m.%d"), datetime.strptime("2024.2.20", "%Y.%m.%d"), 2],
    [5, "하귀1리 1040(제주 애월 하귀 정암 에코빌)", "420", "40", 30, "84.01", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D",
     False,
     datetime.strptime("2024.05.24", "%Y.%m.%d"), datetime.strptime("2024.1.24", "%Y.%m.%d"), 0],
    [6, "오라이동 1390-1(제주 휴림 힐 타운)", "458", "40", 30, "84.01", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D",
     False,
     datetime.strptime("2024.05.24", "%Y.%m.%d"), datetime.strptime("2023.12.24", "%Y.%m.%d"), 0],
    [7, "삼도이동 602-1(제주 아이린아파트 5차)", "290", "40", 30, "84.01", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", 
     "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D",
     False,
     datetime.strptime("2024.05.24", "%Y.%m.%d"), datetime.strptime("2021.10.24", "%Y.%m.%d"), 0]]


    response.status_code = status.HTTP_200_OK 
    homeList=[Home(*data) for data in homes_data] 

    if (sort_request.show_standard == "PROGRESS"):
        filtered_home_list = list(filter(lambda home: home.is_funding_done == True, homeList))
        print(filtered_home_list)
    elif(sort_request.show_standard == "FIN"):
        filtered_home_list = list(filter(lambda home: home.is_funding_done == False, homeList))
        print(filtered_home_list)
    else:
        filtered_home_list = homeList

    return WholeHomeResponseList(filtered_home_list)

@router.get("/home/{home_seq}", response_model=HomeResponse, description="""주택 세부 조회 """)
async def read_item(response:Response, home_seq: int):

    response.status_code = status.HTTP_200_OK 

    home = Home(
        home_seq=1,
        address="도두일동 2619-1(도두 네오하임)",
        sale_price="340",
        funding_current_price="40",
        num_of_people=30,
        width="84.01",
        before_image_url="https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D",
        after_image_url="https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D" ,
        is_funding_done=False,
        funding_done_date=datetime.strptime("2023.10.24", "%Y.%m.%d"),
        funding_open_date=datetime.strptime("2024.10.24", "%Y.%m.%d"),
        funding_last_date=363
    )


    return HomeResponse(home=home)
    


# @router.get("/home/page", response_model=HomeResponseWithPage, description="""주택 페이지 목록""")
# async def read_item_as_page(response:Response, page:Page):
#     # 가상의 데이터라고 가정합니다.
#     page = Page(total_page=3, current=1, total_count=23, chunk=10)
#     homes_data = [
#         [1, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
#         [2, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
#         [3, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
#         [4, "도두일동 2619-1(도두 네오하임)", "네오종합건설㈜", "㈜네오투자개발", True ,True, "84.01", 340, 64, 24, datetime.strptime("2016.10.24", "%Y.%m.%d"),  datetime.strptime("2016.10.24", "%Y.%m.%d"), datetime.strptime("2016.11.07", "%Y.%m.%d"), True, "민간", "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D", None ,False], 
#     ]
#     response.status_code = status.HTTP_200_OK
#     home = Home( homeList=[Home(*data) for data in homes_data])
#     return HomeResponseWithPage(home=home, page=page)
    