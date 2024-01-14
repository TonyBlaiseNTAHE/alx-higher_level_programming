#!/usr/bin/python3

"""
14-model_city_fetch_by_state module
"""

import sqlalchemy
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state, city in \
        session.query(State, City)\
            .filter(State.id == City.state_id).order_by(City.id).all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
