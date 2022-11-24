import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request, Query
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database_crud, db_models
from database import SessionLocal, engine
from schemas import OptionIn, OptionOut, PollsIn, PollsOut, Vote
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
* Add options to a poll.
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

@usersPollsAPI.post("/v1/polls", response_model=PollsOut, summary ="Create a poll", tags=["Polls"])
def create_poll(poll_in: PollsIn, db: Session = Depends(get_users_polls_db)):
    """
    Creates a poll
    """
    try:
        result = {}
        return result
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured. Report this message to support: {e}")

@usersPollsAPI.get("/v1/polls", response_model=List[PollsOut], summary ="Get all active polls and optionally adds the inactive ones", tags=["Polls"])
def get_polls(active : bool = True, db: Session = Depends(get_users_polls_db)):
    """
    Returns all active polls
    and optionally adds the inactive ones
    """
    try:
        result = {}
        return result
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured. Report this message to support: {e}")

@usersPollsAPI.get("/v1/polls/{poll_id}", response_model=PollsOut, summary ="Get a poll given an ID", tags=["Polls"])
def get_poll(poll_id : int, db: Session = Depends(get_users_polls_db)):
    """
    Returns a poll,
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
