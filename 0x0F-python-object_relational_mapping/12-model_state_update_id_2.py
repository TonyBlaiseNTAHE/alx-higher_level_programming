#!/usr/bin/python3

"""
12-model_state_update_id_2 module
"""

import sqlalchemy
from model_state import State, Base
import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state_to_update = session.query(State).filter(State.id == 2).first()
    state_to_update.name = 'New mexico'
    session.commit()
    session.close()
