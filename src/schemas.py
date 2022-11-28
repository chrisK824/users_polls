from pydantic import BaseModel
from typing import List
from datetime import datetime, date


class VoteIn(BaseModel):
    username: str
    poll_id: int
    option_id: int


class VoteOut(VoteIn):
    vote_timestamp: datetime

    class Config:
        orm_mode = True

class OptionIn(BaseModel):
    value: str


class Option(BaseModel):
    id : int
    value: str
    poll_id : int
    votes : List[VoteOut]
    class Config:
        orm_mode = True

class OptionOut(BaseModel):
    id : int
    value: str

class PollsIn(BaseModel):
    title: str
    description: str
    owner: str
    start_date: date
    end_date: date
    options: List[OptionIn]


class PollsOut(PollsIn):
    id: int
    options: list
    class Config:
        orm_mode = True



class PollWinner(BaseModel):
    username: str
