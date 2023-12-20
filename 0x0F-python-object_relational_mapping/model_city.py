#!/usr/bin/python3

"""
model_city module
"""

from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """city class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
