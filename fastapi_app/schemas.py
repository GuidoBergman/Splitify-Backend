from pydantic import BaseModel
from datetime import datetime
from typing import Optional



class ExpenditureBase(BaseModel):
	id_user: int
	amount: float
	id_group: int
	description : str

class Expenditure(ExpenditureBase):
	time_created: str

    