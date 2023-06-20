"""
this module contains the class DBStorage
"""
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """
    new storage system
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        constructor method for the new
        storage engine
        """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        this func should return dictionary with all objects depending
        on the clas name arg(cls)
        """
        if cls:
            objs = self.__session.query(classes[cls])
        else:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Review).all()

        a_dict = {}
        for obj in objs:
            k = '{}.{}'.format(type(obj).__name__, obj.id)
            a_dict[k] = obj
        return a_dict

    def new(self, obj):
        """
        this func will add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all the changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if the obj arg
        passed is not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        reloads all the data from the database
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine))
        self.__session = Session

    def close(self):
        """
        remove the current session
        """
        self.__session.close()
