from pydantic import BaseModel, Optional
from typing import List
from datetime import datetime


class OptionIn(BaseModel):
    value: str

class OptionOut(OptionIn):
    id: int

    class Config:
        orm_mode = True


class PollsIn(BaseModel):
    name: str
    description: str
    owner : str
    start_date: Optional[datetime] = None
    end_date: datetime
    options: Optional[List[OptionIn]] = []


class PollsOut(PollsIn):
    id: int

    class Config:
        orm_mode = True


class VoteIn(BaseModel):
    username : str
    poll_id : PollsOut.id
    option_id : OptionOut.id

class VoteOut(VoteIn):
    vote_timestamp : datetime

    class Config:
        orm_mode = True
