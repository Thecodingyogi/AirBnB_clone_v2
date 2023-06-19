#!/usr/bin/python3
"""
City Module for HBNB project
It will represent the cities table that will have two
columns i.e name and state_id which is a foreign key
connecting the cities and the states table
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """
    contains name and state_id attributes
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
