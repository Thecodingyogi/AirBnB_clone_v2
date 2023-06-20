#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from models import storage
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """
    A base class for all hbnb models
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        if self.created_at is None:
            self.created_at = self.updated_at
        storage.new(self)
        storage.save()

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
