from fastapi import File, UploadFile, APIRouter, Response, status

router = APIRouter()

@router.post("/ai/image/create-new")
def create_image_and_response_image(home_seq):
    # before/after 하나씩 db에 저장
    pass 





@router.post("/ai/image/convert-image")
def convert_image_with_already_exist(home_seq, before_image_url):
    pass



