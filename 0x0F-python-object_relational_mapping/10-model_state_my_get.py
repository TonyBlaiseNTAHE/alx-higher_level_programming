#!/usr/bin/python3

"""
10-model_state_my_get module
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)

    state_name = sys.argv[4]
    session = Session(engine)
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print('{}'.format(state.id))
    else:
        print("Not found")
