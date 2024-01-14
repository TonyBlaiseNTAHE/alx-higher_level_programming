#!/usr/bin/python3

"""
8-model_state_fetch_first module
"""

import sys
import sqlalchemy
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).filter(State.id == 1).all():
        if state == "":
            print('Nothing')
        else:
            print('{}: {}'.format(state.id, state.name))

    session.close()
