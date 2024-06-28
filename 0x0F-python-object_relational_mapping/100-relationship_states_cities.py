#!/usr/bin/python3
"""
creates the State "California" with the city "San Francisco"
from the database 'hbtn_0e_100_usa'
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    California = State(name="California")
    San_francisco = City(name='San Francisco', state=California)

    session.add(California)
    session.add(San_francisco)
    session.commit()
