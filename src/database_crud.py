from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import db_models
from schemas import PollsIn, OptionIn, OptionOut


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
    polls = list(db.query(db_models.Poll).all())
    for poll in polls:
        print(poll.title)
        print(poll.id)
        print(poll.start_date)
        poll.options = []
        # for option in list(db.query(db_models.Option).filter(db_models.Option.poll_id==poll.id).all()):
        #     option_out = OptionOut(id = option.id, value=option.value)
        #     poll.options.append(option_out)

    return polls
    # options = list(db.query(db_models.Option).all())
    # for option in options:
    #     print(option.id)
    #     print(option.value)
    #     print(option.poll_id)
