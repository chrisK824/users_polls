from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import text
import db_models
from schemas import PollsIn, OptionIn, VoteIn
from datetime import datetime


class DuplicateError(Exception):
    pass


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


def get_polls(inactive: bool, db: Session):
    if inactive:
        polls = db.query(db_models.Poll).all()
    else:
        polls = db.query(db_models.Poll).filter(db_models.Poll.end_date >= datetime.utcnow(
        )).filter(db_models.Poll.start_date <= datetime.utcnow()).all()
    return polls


def get_poll(poll_id: int, db: Session):
    poll = db.query(db_models.Poll).filter(
        db_models.Poll.id == poll_id).first()
    return poll


def post_vote(vote: VoteIn, db: Session):
    option = db.query(db_models.Option).filter(db_models.Option.id == vote.option_id).filter(
        db_models.Option.poll_id == vote.poll_id).first()
    if option:
        try:
            db_vote_entry = db_models.Vote(
                username=vote.username,
                option_id=vote.option_id,
                poll_id=vote.poll_id
            )
            db.add(db_vote_entry)
            db.commit()
            return db_vote_entry
        except IntegrityError:
            db.rollback()
            raise DuplicateError(
                f"User {vote.username} has already voted for poll {vote.poll_id}")
    else:
        raise ValueError(
            f"There is no option {vote.option_id} for poll {vote.poll_id}")


def get_votes(poll_id: int, db: Session):
    query = """SELECT username, vote_timestamp, title, value
    FROM votes INNER JOIN options ON votes.option_id = options.id
    INNER JOIN polls ON options.poll_id = polls.id
    WHERE votes.poll_id = (%s);"""
    votes = db.execute(text(query % str(poll_id))).fetchall()
    return votes
