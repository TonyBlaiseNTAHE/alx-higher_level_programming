#!/usr/bin/python3

"""
12-model_state_update_id_2 module
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    session = Session(engine)

    deleted_state = session.query(State).filter(State.name.like('%a%'))
    deleted_state.delete()
    session.commit()
    session.close()
