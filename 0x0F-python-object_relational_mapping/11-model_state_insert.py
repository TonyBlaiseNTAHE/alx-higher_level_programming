#!/usr/bin/python3

"""
11-model_state_insert
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(State(name='Louisiana'))
    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    session.commit()
    print(f'{new_state.id}')
    session.close()
