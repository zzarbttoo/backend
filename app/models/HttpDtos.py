from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json import LetterCase

#Page
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Page:
    total: int  # 전체 페이지 수
    current: int # 현재 페이지 

#Home
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Home:
    home_seq:int
    address: str #주소 
    construction_company:str #시공사
    executing_agency:str #시행사
    type_sale: bool #분양? -> true: 분양, false : 임대
    is_private:bool #민간? -> true: 민간, false : 공공 
    scale: str #규모별
    sale_price: int #분양가(백만원)
    number_of_sale_units: int #총분양가구수
    number_of_unsold_units: int #미분양가구수(당월)
    subscription_date_for_sale: str #분양 청약일
    contract_closing_date: str #계약 마감일 
    scheduled_move_in_date: str #입주 예정일 
    is_completion_status: bool #준공? -> true : 준공 false: 미준공
    land_type: str #택지 종류
    # before_image_url:str #before 이미지 사진, db저장 
    # after_image_url:str #after 이미지 사진, db저장(null 로 오면 없는 것..)


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
    
   


