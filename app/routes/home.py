# controllers/items.py
from fastapi import APIRouter, Response, status

router = APIRouter(prefix="/api")

base_64_url = "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"


from datetime import datetime
from app.models.HttpDtos import Home, Page, HomeResponseWithPage, WholeHomeResponseList, HomeResponse, SortRequest

@router.get("/home/", response_model=WholeHomeResponseList, description="""주택 전체 목록 """)
async def read_items(response:Response):

    homes_data = [
    [1, "도두일동 2619-1(도두 네오하임)", "340", "40", 30, "84.01", 
     base_64_url, 
     base_64_url,
     True,
     datetime.strptime("2023.10.24", "%Y.%m.%d"), datetime.strptime("2024.10.24", "%Y.%m.%d"), 363],
    [2, "하귀2리 1437(하귀 코아루오션뷰)", "391", "80", 50, "78.9661", 
     base_64_url, 
     base_64_url,
     True,
     datetime.strptime("2023.08.24", "%Y.%m.%d"), datetime.strptime("2023.09.24", "%Y.%m.%d"), 362],
    [3, "도두일동 2619-2(도두 네오하임 주상복합 아파트 2차", "375", "100", 2, "84.34", 
 base_64_url, 
     base_64_url,
     True,
     datetime.strptime("2023.07.24", "%Y.%m.%d"), datetime.strptime("2024.08.22", "%Y.%m.%d"), 361],
    [4, "도두일동 2619-1(도두 네오하임)", "370", "40", 30, "84.01", 
    base_64_url, 
    base_64_url, 
     False,
     datetime.strptime("2024.06.24", "%Y.%m.%d"), datetime.strptime("2024.2.20", "%Y.%m.%d"), 2],
    [5, "하귀1리 1040(제주 애월 하귀 정암 에코빌)", "420", "40", 30, "84.01", 
     False,
    base_64_url, 
    base_64_url, 
     datetime.strptime("2024.05.24", "%Y.%m.%d"), datetime.strptime("2024.1.24", "%Y.%m.%d"), 0],
    [6, "오라이동 1390-1(제주 휴림 힐 타운)", "458", "40", 30, "84.01", 
    base_64_url, 
    base_64_url, 
     False,
     datetime.strptime("2024.05.24", "%Y.%m.%d"), datetime.strptime("2023.12.24", "%Y.%m.%d"), 0],
    [7, "삼도이동 602-1(제주 아이린아파트 5차)", "290", "40", 30, "84.01", 
    base_64_url, 
    base_64_url, 
     False,
     datetime.strptime("2024.05.24", "%Y.%m.%d"), datetime.strptime("2021.10.24", "%Y.%m.%d"), 0]]


    response.status_code = status.HTTP_200_OK 
    homeList=[Home(*data) for data in homes_data] 

    return WholeHomeResponseList(homeList)

    # if (sort_request.show_standard == "PROGRESS"):
    #     filtered_home_list = list(filter(lambda home: home.is_funding_done == True, homeList))
    #     print(filtered_home_list)
    # elif(sort_request.show_standard == "FIN"):
    #     filtered_home_list = list(filter(lambda home: home.is_funding_done == False, homeList))
    #     print(filtered_home_list)
    # else:
    #     filtered_home_list = homeList

    # return WholeHomeResponseList(filtered_home_list)

@router.get("/home/target/{home_seq}", response_model=HomeResponse, description="""주택 세부 조회 """)
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
    