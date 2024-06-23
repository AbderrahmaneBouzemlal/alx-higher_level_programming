#!/usr/bin/python3
"""
Module that lists all State objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_state(username, password, dbname):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.execute(select(State).order_by(State.id.asc()).all())
    for row in result:
        print(f"{row.State.id}:{row.State.name}")


if __name__ == "__main__":
    USERNAME = argv[1]
    PASSWORD = argv[2]
    DBNAME = argv[3]
    list_state(USERNAME, PASSWORD, DBNAME)
