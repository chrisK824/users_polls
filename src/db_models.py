from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Date, UniqueConstraint
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship


class Poll(Base):
    __tablename__ = "polls"
    id = Column(Integer, primary_key=True, index=False)
    title = Column(String)
    description = Column(String)
    owner = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    options = relationship("Option", back_populates="poll", cascade="all,delete")


class Option(Base):
    __tablename__ = "options"
    id = Column(Integer, primary_key=True, index=False)
    value = Column(String)
    poll_id = Column(Integer, ForeignKey("polls.id"))

    poll = relationship("Poll", back_populates="options", cascade="all,delete")
    votes = relationship("Vote", back_populates="option", cascade="all,delete")


class Vote(Base):
    __tablename__ = "votes"
    username = Column(String, primary_key=True, index=False)
    vote_timestamp = Column(DateTime, default=func.now())
    poll_id = Column(Integer, ForeignKey("polls.id"))
    option_id = Column(Integer, ForeignKey("options.id"))
    __table_args__ = (UniqueConstraint(
        'username', 'poll_id', name='username_poll'),)

    option = relationship("Option", back_populates="votes", cascade="all,delete")
