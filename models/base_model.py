#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
import uuid
from os import getenv
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """
    A base class for all hbnb models
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of class BaseModel
        prints: "[<class name>] (<self.id>)<self.__dict__>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """
        return string rep of BaseModel
        """
        return (self.__str__())

    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]

        return new_dict
