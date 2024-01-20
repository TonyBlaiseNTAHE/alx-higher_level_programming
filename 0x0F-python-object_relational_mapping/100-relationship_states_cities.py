#!/usr/bin/python3

"""
100-relationship_states_cities module
"""

from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    city = City(name='San Francisco')
    state = State(name='California')
    state.cities.append(city)
    session.add_all([state, city])
    session.commit()
    session.close()
