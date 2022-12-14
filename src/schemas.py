from pydantic import BaseModel, Field, EmailStr
from typing import List
from datetime import datetime, date


class VoteIn(BaseModel):
    email: EmailStr
    poll_id: int = Field(..., gt=0)
    option_id: int = Field(..., gt=0)


class VoteOut(VoteIn):
    vote_timestamp: datetime

    class Config:
        orm_mode = True


class VotesOut(BaseModel):
    email: str
    vote_timestamp: datetime
    title: str
    value: str


class VoteOut(VoteIn):
    vote_timestamp: datetime

    class Config:
        orm_mode = True


class OptionIn(BaseModel):
    value: str


class Option(BaseModel):
    id: int
    value: str
    poll_id: int
    votes: List[VoteOut]

    class Config:
        orm_mode = True

class OptionOut(BaseModel):
    id: int
    value: str
    class Config:
        orm_mode = True

class PollsIn(BaseModel):
    title: str
    description: str
    owner: str
    start_date: date
    end_date: date
    options: List[OptionIn]


class PollsOut(PollsIn):
    id: int
    options: List[OptionOut]

    class Config:
        orm_mode = True

