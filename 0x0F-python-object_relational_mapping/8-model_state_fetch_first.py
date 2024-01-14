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
    obj = session.query(State).order_by(State.id).first()
    if obj:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')

    session.close()
