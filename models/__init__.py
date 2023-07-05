#!/usr/bin/python3
"""
This module automatically instantiates the models package
"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City

if getenv("HBNB_TYPE_STORAGE") == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
