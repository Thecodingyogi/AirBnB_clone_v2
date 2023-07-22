#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ represents Amenity"""
    __tablename__ = "amenities"
    __table_args__ = (
                      {'mysql_default_charset': 'latin1'})
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity,
                                       viewonly=False)

    def __init__(self, *args, **kwargs):
        """Initialize Ammenity class"""
        super().__init__(*args, **kwargs)
