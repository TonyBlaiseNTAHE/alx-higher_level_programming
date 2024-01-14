#!/usr/bin/python3

"""
10-model_state_my_get module
"""

import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    stat = sys.argv[4]
    session = Session(engine)
    state = session.query(State).filter(State.name == stat).first()
    if state:
        print('{}'.format(state.id))
    else:
        print('Not found')

    session.close()
