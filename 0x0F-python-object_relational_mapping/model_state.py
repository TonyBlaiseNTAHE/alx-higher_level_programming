#!/usr/bin/python3
"""
model_state module
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=True, primary_key=True,
                autoincrement=True)
    name = Column(String(128), nullable=True)
    