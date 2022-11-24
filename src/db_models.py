from sqlalchemy import Column, DateTime, Integer, String
# from sqlalchemy.sql import func
from database import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=False)
    age = Column(Integer)
    name = Column(String)
    surname = Column(String)

class Polls(Base):
    __tablename__ = "polls"
    id = Column(Integer, primary_key=True, index=False)
    name = Column(Integer)
    description = Column(String)
    # foreign key relation for user id

class Votes(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True, index=False)
    name = Column(Integer)
    description = Column(String)
    # foreign key relation for user id
    # foreign key relation for poll id
