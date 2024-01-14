#!/usr/bin/python3

"""
model_city module
"""

import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, String
from model_state import Base
from sqlalchemy.orm import relationship

class City(Base):
    """city class"""
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
