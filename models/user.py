#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship('Place', backref='user', cascade='delete')
