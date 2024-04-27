#!/usr/bin/python3
"""DBStorage class defenition"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base
import models


class DBStorage:
    __engine = None
    __session = None
    __classes = {
        'City': City,
        'User': User,
        'Place': Place,
        'State': State,
        'Review': Review,
        'Amenity': Amenity
    }

    def __init__(self):
        db_user = os.getenv('HBNB_MYSQL_USER')
        db_pwd = os.getenv('HBNB_MYSQL_PWD')
        db_host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f"mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db_name}",
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns all records in the db
        if cls is set return a filtered list
        depending on cls
        """
        dictionary = {}
        classes = [k for k in self.__classes.keys()]
        if cls:
            try:
                cls = self.__classes[cls]
            except KeyError:
                pass
            else:
                classes = [cls]

        for obj in classes:
            for instance in self.__session.query(obj).all():
                key = f"{instance.__class__.__name__}.{str(instance.id)}"
                dictionary[key] = instance
        return dictionary

    def new(self, obj):
        """add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj if exists from db"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        create all tables in the database
        create the current database session
        """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
