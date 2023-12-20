#!/usr/bin/python3

"""
8-model_state_fetch_one module
"""
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    session = Session(engine)

    for state in session.query(State).filter(State.id == 1):
        if session == "":
            print()
        print('{}: {}'.format(state.id, state.name))

    session.close()
