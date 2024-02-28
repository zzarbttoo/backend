from fastapi import File, UploadFile, APIRouter, Response, status
from app.models.HttpDtos import CreateImageRequest, CreateImageResponse, ConvertImageRequest, ConvertImageAndInsertHomeResponse, Home

from datetime import datetime

router = APIRouter(prefix="/api")

@router.post("/ai/image/create-new", response_model= CreateImageResponse, description="이미지가 없는 경우 새로운 이미지를 생성 및 db에 저장하는 api(before 사진에 저장)")
def create_image_and_response_image(response:Response, req:CreateImageRequest):

    # before/after 하나씩 db에 저장
    response.status_code = status.HTTP_200_OK 
    return CreateImageResponse(home_seq=1, image_url="https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D")



@router.post("/ai/image/convert-image", response_model=ConvertImageAndInsertHomeResponse, description="")
def convert_image_with_already_exist(response:Response, req:ConvertImageRequest):

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

    response.status_code = status.HTTP_200_OK 
    return ConvertImageAndInsertHomeResponse(home=home)



