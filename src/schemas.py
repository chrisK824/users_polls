from pydantic import BaseModel

class UserIn(BaseModel):
    name : str
    surname : str
    age : int
    class Config:
        orm_mode = True

class UserOut(UserIn):
    id : int
    class Config:
        orm_mode = True


