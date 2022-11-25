from pydantic import BaseModel
from typing import List
from datetime import datetime


class VoteIn(BaseModel):
    username: str
    poll_id: int
    option_id: int


class VoteOut(VoteIn):
    vote_timestamp: datetime

    class Config:
        orm_mode = True

class Option(BaseModel):
    id: int
    value: str
    votes : List[VoteOut]
    class Config:
        orm_mode = True


class PollsIn(BaseModel):
    title: str
    description: str
    owner: str
    start_date: datetime
    end_date: datetime
    options: List[str]


class PollsOut(PollsIn):
    id: int

    class Config:
        orm_mode = True



class PollWinner(BaseModel):
    username: str
