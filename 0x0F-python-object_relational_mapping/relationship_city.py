#!/usr/bin/python3
"""
This file contain the class definition of the city class
and the base instance
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The City id of the class
        name (str): The City name of the class

    """
    __tablename__ = "cities"

    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True
        )
    name = Column(
        String(128),
        nullable=False
        )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
        )

    state = relationship('State', back_populates='cities')
