from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Bse

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
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSLQ_PWD"), getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        objects = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            for cls in Base.__subclasses__():
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        if obj:
            self.__session.add(obj)
    def save(self):
        self.__session.commit()
    def delete(self obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine), expire_on_commit=False)
        self.__session = Session()
