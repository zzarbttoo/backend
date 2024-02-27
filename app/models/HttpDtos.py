from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json import LetterCase

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass()
class Request1:
    id_seq: int
    contract_seq: int
    model_name:str

