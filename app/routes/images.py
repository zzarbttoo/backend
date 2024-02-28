from fastapi import File, UploadFile, APIRouter, Response, status
from app.models.HttpDtos import CreateImageRequest, CreateImageResponse, ConvertImageRequest, ConvertImageAndInsertHomeResponse

router = APIRouter(prefix="/api")

@router.post("/ai/image/create-new", response_model= CreateImageResponse, description="이미지가 없는 경우 새로운 이미지를 생성 및 db에 저장하는 api(before 사진에 저장)")
def create_image_and_response_image(response:Response, req:CreateImageRequest):

    # before/after 하나씩 db에 저장
    response.status_code = status.HTTP_200_OK 
    return None
    # return CreateImageResponse(home_seq=1, image_url=)





@router.post("/ai/image/convert-image", response_model=ConvertImageAndInsertHomeResponse, description="")
def convert_image_with_already_exist(reponse:Response, req:ConvertImageRequest):
    return None



