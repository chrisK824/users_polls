import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, Query
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database_crud, db_models
from database import SessionLocal, engine
from schemas import UserIn, UserOut
from typing import List

db_models.Base.metadata.create_all(bind=engine)

def get_users_polls_db():
    users_polls_db = SessionLocal()
    try:
        yield users_polls_db
    finally:
        users_polls_db.close()

description = """
Users polls API helps people
to easily create and view polls
as well as vote on a poll and see
votes for a poll.

#### Users

You will be able to:

* Create new poll.
* List open polls.
* Vote on a poll.
* Show poll votes.
* Select a random winner from a poll option.
"""

usersPollsAPI = FastAPI(
    title='Users polls API',
    description=description,
    contact={
        "name": "Christos Karvouniaris",
        "email": "christos.karvouniaris247@gmail.com",
        "url" : "https://www.linkedin.com/in/chriskarvouniaris/"
    },
    version="1.0.0",
    docs_url="/v1/documentation",
    redoc_url="/v1/redocs"
)

usersPollsAPI.add_middleware(CORSMiddleware, allow_origins=['*'])

@usersPollsAPI.post("/v1/users", response_model=UserOut, summary ="Create a user for the poll app", tags=["Users"])
def get_users(user_in: UserIn, db: Session = Depends(get_users_polls_db)):
    """
    Creates a user for the poll app
    """
    try:
        result = {}
        return result
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured. Report this message to support: {e}")

@usersPollsAPI.get("/v1/users", response_model=List[UserOut], summary ="Get all users of the poll app", tags=["Users"])
def get_users(db: Session = Depends(get_users_polls_db)):
    """
    Returns all users of the poll app
    """
    try:
        result = {}
        return result
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured. Report this message to support: {e}")

@usersPollsAPI.get("/v1/users/{user_id}", response_model=UserOut, summary ="Get a users of the poll app given an ID", tags=["Users"])
def get_users(user_id : int, db: Session = Depends(get_users_polls_db)):
    """
    Returns a user of the poll app,
    given an ID.
    """
    try:
        result = {}
        return result
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured. Report this message to support: {e}")

if __name__ == '__main__':
    uvicorn.run(usersPollsAPI, host="0.0.0.0", port=9999)
