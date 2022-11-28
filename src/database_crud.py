from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import db_models
from schemas import PollsIn, OptionIn
from datetime import datetime


def create_option(option: OptionIn, poll_id, db: Session):
    option_record = db_models.Option(value=option.value, poll_id=poll_id)
    db.add(option_record)

def create_poll(poll: PollsIn, db: Session):
    db_poll_entry = db_models.Poll(
        title=poll.title,
        description=poll.description,
        owner=poll.owner,
        start_date=poll.start_date,
        end_date=poll.end_date
    )
    db.add(db_poll_entry)
    db.flush()
    created_poll_entry_id = db_poll_entry.id
    for option in poll.options:
        create_option(option=option, poll_id=created_poll_entry_id, db=db)
    db.commit()


def get_polls(inactive : bool, db: Session):
    if inactive:
        polls = db.query(db_models.Poll).all()
    else:
        polls= db.query(db_models.Poll).filter(db_models.Poll.end_date >= datetime.utcnow()).filter(db_models.Poll.start_date <= datetime.utcnow()).all()
    return polls

def get_poll(poll_id: int, db: Session):
    poll = db.query(db_models.Poll).filter(db_models.Poll.id == poll_id).first()
    return poll
