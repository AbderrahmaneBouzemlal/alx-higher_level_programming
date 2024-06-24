#!/usr/bin/python3
"""
This script a State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    state_name = argv[4]
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    instances = session.query.get(State).\
        filter(State.name == state_name).\
        order_by(State.id)
    if instance is None:
        print('Not found')
    for instance in instances:
        print('{0}'.format(instance.id))
