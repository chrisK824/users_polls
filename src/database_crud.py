from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import db_models
from schemas import PollsIn, Option

def create_option(option, poll_id, db):
    option_record = db_models.Option(
        value = option,
        poll_id = poll_id
    )
    db.add(option_record)
    db.commit()


def create_poll(poll : PollsIn, db):
    poll = db_models.Poll(
        title = poll.title,
        description = poll.description,
        owner = poll.owner,
        start_date = poll.start_date,
        end_date =poll.end_date
    )
    db.add(poll)
    # created_poll_entry = db.add(poll)
    # db.commit()
    # created_poll_entry_id = created_poll_entry.inserted_primary_key

    # for value in poll.options:
    #     create_option(option=value, poll_id=created_poll_entry_id)

    db.commit()
    # db.refresh()