from pydantic import BaseModel, Optional
from typing import List
from datetime import datetime


class OptionIn(BaseModel):
    value: str

    class Config:
        orm_mode = True


class OptionOut(OptionIn):
    id: int

    class Config:
        orm_mode = True


class PollsIn(BaseModel):
    name: str
    description: str
    start_date: Optional[datetime] = None
    end_date: datetime
    options: Optional[List[OptionOut]] = []

    class Config:
        orm_mode = True


class PollsOut(PollsIn):
    id: int

    class Config:
        orm_mode = True


class Vote(BaseModel):
    username : str
    poll_id : int
    option : int

    class Config:
        orm_mode = True
