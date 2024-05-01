#!/usr/bin/python3
"""DBStorage class defenition"""

import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (
    sessionmaker,
    scoped_session,
    relationship
)
from models.base_model import Base
from models import classes


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
        results = []
        if cls:
            try:
                clsobj = classes[cls]
            except KeyError:
                pass
            else:
                objs = {cls: clsobj}

        for obj in objs.values():
            results.extend(self.__session.query(obj).all())
        for instance in results:
            key = f"{type(instance).__name__}.{instance.id}"
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

