from .karlo import Karlo


def get_img_str():

    proxy_url = "http://krmp-proxy.9rum.cc:3128"
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }

    api = Karlo(service_key = "09aca835cbc4ba2e3164cf76632a1b18")

    # 프롬프트에 사용할 제시어
    # text = "A picture of an empty house in Jeju Island"
    text = "A picture of an empty house in Jeju Island"

    # 이미지 생성하기 REST API 호출
    img_dict = api.text_to_image(text, 1)

    # 생성된 이미지 정보
    img_str = img_dict.get("images")[0].get('image')

    return img_str

