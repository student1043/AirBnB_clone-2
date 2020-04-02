#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    state_id = Column(string(60), nullable=False, ForeignKey(states.id))
    name = Column(string(128), nullable=False)
    places = relationship("Place", backref="cities")
