# import requests
# import json
# import io
# import base64
# import urllib
# from PIL import Image

# # [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
# # REST_API_KEY = '${REST_API_KEY}'

# # 이미지 변환하기
# def inpainting(image, mask):
#     r = requests.post(
#         'https://api.kakaobrain.com/v2/inference/karlo/inpainting',
#         json = {
#             'image': image,
#             'mask': mask,
#             'prompt' : """
#             the house look warm and cozy
#             """,
#         },
#         headers = {
#             'Authorization': f'',
#             'Content-Type': 'application/json'
#         }
#     )
#     # 응답 JSON 형식으로 변환
#     response = json.loads(r.content)
#     return response

# # Base64 인코딩
# def imageToString(img):
#     img_byte_arr = io.BytesIO()
#     img.save(img_byte_arr, format='PNG')
#     my_encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
#     return my_encoded_img

# # image_url = "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D"
# # response = requests.get(image_url)
# # print(response.content)
# # img = Image.open(io.BytesIO(response))

# # image_url = "https://mk.kakaocdn.net/dna/karlo/image/2024-02-28/15/5a7cef75-763b-470f-b777-ae266853a458.webp?credential=smxRqiqUEJBVgohptvfXS5JoYeFv4Xxa&expires=1709103142&signature=%2FVen9pBIBmtvTZMw2vNj637B8uQ%3D"
# # response = requests.get(image_url)


# def convert_result():
#     img = Image.open(BytesIO())

#     width, height = img.size
#     black_image = Image.new("RGBA", (width, height), (0, 0, 0))

#     img_base64 = imageToString(img)
#     mask_base64 = imageToString(black_image)

#     # 이미지 변환하기 REST API 호출
#     response = inpainting(img_base64,mask_base64)
#     print(response)

#     # 응답의 첫 번째 이미지 생성 결과 출력하기
#     result = Image.open(requests.get(response.get("images")[0].get("image")))


#     result.show()