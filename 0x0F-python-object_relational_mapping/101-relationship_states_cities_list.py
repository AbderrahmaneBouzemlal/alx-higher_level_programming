#!/usr/bin/python3
"""
This script lists all State objects,
and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Access the database and get the states
    and the corresponding City
    """
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State, City).join(City, City.state_id == State.id).order_by(State.id, City.id)
    current = None
    for _s, _c in query.all():
    	if _s.id != current:
    		if current is not None:
    			print()
    		print("{:d}: {}||".format(_s.id, _s.name))
    		current = _s.id
    	print("    {:d}: {}".format(_c.id, _c.name))

    session.commit()
    session.close()
