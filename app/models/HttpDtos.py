from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json import LetterCase

from datetime import datetime

#SortRequest
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SortRequest:
    sort_standard:str #END_DATE 
    show_standard:str #ALL, FIN, PROGRESS


#Page
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Page:
    total_page: int  # 전체 페이지 수
    current: int # 현재 페이지 
    total_count: int #전체 갯수 
    chunk: int #한 페이지당 갯수 

#Home
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Home:
    home_seq:int
    address: str #주소 
    sale_price: int #분양가(백만원), 펀딩가
    funding_current_price:int #펀딩가(백만원)
    num_of_people:int #참여 인원
    width:str #면적
    before_image_url:str #before 이미지 사진, db저장
    after_image_url:str #after 이미지 사진, db저장(null 로 오면 생성 가능)
    is_funding_done:bool #funding 완료 여부
    funding_done_date:datetime #funding 완료 일자 
    funding_open_date:datetime #funding 시작 일자 
    funding_last_date:str #funding D-Day


#Response
from typing import List

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class HomeResponseWithPage:
    homeList: List[Home]
    page : Page
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class WholeHomeResponseList:
    homeList: List[Home]

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class HomeResponse:
    home:Home


#Request
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateImageRequest:
    home_seq:int
   

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CreateImageResponse:
    home_seq:int 
    image_url:str

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ConvertImageRequest():
    home_seq:int
    before_image_url:str
    corp_list:List #요구사항들 리스트로 받음, nullable


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ConvertImageAndInsertHomeResponse():
    home:Home
    
   


