#!/usr/bin/python3
"""
City Module for HBNB project
It will represent the cities table that will have two
columns i.e name and state_id which is a foreign key
connecting the cities and the states table
"""
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    contains name and state_id attributes
    """
    __tablename__ = "cities"
    __table_args__ = (
                      {'mysql_default_charset': 'latin1'})
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
