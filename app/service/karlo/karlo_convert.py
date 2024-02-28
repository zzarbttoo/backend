import requests
import json
import io
import base64
import urllib
from PIL import Image

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
# REST_API_KEY = '${REST_API_KEY}'
import base64

proxy_url = "http://krmp-proxy.9rum.cc:3128"




# 이미지 변환하기
def inpainting(image, mask):

    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    target_url='https://api.kakaobrain.com/v2/inference/karlo/inpainting'

    r = requests.post(
        target_url
        ,
        json = {
            'image': base64.encodebytes(image).decode('ascii'),
            'mask' : mask,
            'prompt' : """
            the house look warm and cozy
            """,
            'return_type' : 'base64_string'
        },
        headers = {
            'Authorization': f'KakaoAK 09aca835cbc4ba2e3164cf76632a1b18',
            'Content-Type': 'application/json'
        },
        proxies=proxies
        
    )


    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    print(response)

    return response

# Base64 인코딩
def imageToString(img):
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    my_encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return my_encoded_img

from io import BytesIO


def convert_result(base64_str:str):

    image_data = base64.b64decode(base64_str)
    img = Image.open(BytesIO(image_data))

    width, height = img.size
    black_image = Image.new("RGBA", (width, height), (0, 0, 0))


    # img_base64 = imageToString(img)
    mask_base64 = imageToString(black_image)

    # 이미지 변환하기 REST API 호출
    response = inpainting(image_data, mask_base64)
    image_url = response.get("images")[0].get("image")

    return image_url


from urllib import request

def convert_image_from_url(url):
    try:
        url = "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D"
        # URL에서 이미지 가져오기
        # 가져온 이미지를 BytesIO로 읽기
        image_data = request.urlopen(url)


    except Exception as e:
        print("Error:", e)
