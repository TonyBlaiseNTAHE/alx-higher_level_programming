#!/usr/bin/python3

"""
13-model_state_delete_a
"""

import sys
from model_state import Base, State
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
