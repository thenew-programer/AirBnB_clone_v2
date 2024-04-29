#!/usr/bin/python3
"""DBStorage class defenition"""

import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import classes
import models


class DBStorage:
    ''' DBStorage Class

    __engine (sqlalchemy.engine): hold the db engine

    __session (sqlalchemy.orm.Session): hold the session
    '''
    __engine = None
    __session = None

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
        objs = classes.copy()
        if cls:
            print(f"cls = {cls}")
            try:
                clsobj = classes[cls]
            except KeyError:
                pass
            else:
                objs = {cls: clsobj}
                print(f"objs = {objs}")

        for obj in objs.values():
            print(f"obj = {obj.__class__.__name__}")
            for instance in self.__session.query(obj).all():
                key = f"{type(instance).__class__.__name__}.{str(instance.id)}"
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
