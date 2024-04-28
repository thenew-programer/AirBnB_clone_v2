#!/usr/bin/python3
""" State Module for HBNB project """

import os
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_STORAGE_TYPE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', passive_deletes=True, backref='state')
    else:
        name = ''

        @property
        def cities(self):
            """
            cities getter to retreive cities
            related to the current state
            """
            cities = []
            for value in models.storage.all().values():
                try:
                    if value.state_id == self.id:
                        cities.append(value)
                except AttributeError:
                    pass
            return cities
