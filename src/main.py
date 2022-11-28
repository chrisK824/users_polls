import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Query
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database_crud, db_models
from database import SessionLocal, engine
from schemas import PollsIn, PollsOut, VoteIn, VoteOut,PollWinner, VotesOut
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

@usersPollsAPI.post("/v1/polls", summary ="Create a poll", tags=["Polls"])
def create_poll(poll_in: PollsIn, db: Session = Depends(get_users_polls_db)):
    """
    Creates a poll
    """
    try:
        database_crud.create_poll(poll_in, db)
        result = {"result" : f"{poll_in.owner} your poll with title '{poll_in.title}' has been created successfully and will be valid from {poll_in.start_date} until {poll_in.end_date}"}
        return result
    except database_crud.InactivePollError as e:
        raise HTTPException(status_code=403, detail=f"{e}")
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured. Report this message to support: {e}")

@usersPollsAPI.get("/v1/polls", response_model=List[PollsOut], summary ="Get all active polls and optionally adds the inactive ones", tags=["Polls"])
def get_polls(inactive : bool = False, db: Session = Depends(get_users_polls_db)):
    """
    Returns all active polls
    and optionally adds the inactive ones
    """
    try:
        result = database_crud.get_polls(inactive, db)
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
        result = database_crud.get_poll(poll_id=poll_id, db=db)
        return result
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured. Report this message to support: {e}")

@usersPollsAPI.delete("/v1/polls/{poll_id}", summary ="Delete a poll given an ID", tags=["Polls"])
def delete_poll(poll_id : int, db: Session = Depends(get_users_polls_db)):
    """
    Deletes a poll,
    given an ID.
    """
    try:
        database_crud.delete_poll(poll_id=poll_id, db=db)
        return {"result" : f"Poll with ID {poll_id} has been deleted"}
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured. Report this message to support: {e}")

@usersPollsAPI.get("/v1/votes", response_model=List[VotesOut], summary ="Get votes for a given poll ID", tags=["Votes"])
def get_votes(poll_id : int = Query(ge=1), db: Session = Depends(get_users_polls_db)):
    """
    Returns votes for a,
    given poll ID.
    """
    try:
        result = database_crud.get_votes(poll_id=poll_id, db=db)
        return result
    except HTTPException as e:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured. Report this message to support: {e}")

@usersPollsAPI.post("/v1/votes", response_model=VoteOut, summary ="Vote for an option of a given poll ID", tags=["Votes"])
def vote_for_poll(vote : VoteIn, db: Session = Depends(get_users_polls_db)):
    """
    Votes as a username for
    an option of a,
    given poll ID.
    """
    try:
        result = database_crud.post_vote(vote=vote, db=db)
        return result
    except HTTPException as e:
        raise
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"{e}")
    except database_crud.InactivePollError as e:
        raise HTTPException(status_code=403, detail=f"{e}")
    except database_crud.DuplicateError as e:
        raise HTTPException(status_code=403, detail=f"{e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured. Report this message to support: {e}")

@usersPollsAPI.get("/v1/polls/{poll_id}/winner", response_model=PollWinner, summary ="Select random username as winner for a given poll ID", tags=["Polls winners"])
def get_poll_winner(poll_id : int = Query(ge=1), db: Session = Depends(get_users_polls_db)):
    """
    Select random username
    as winner for a given poll ID.
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
