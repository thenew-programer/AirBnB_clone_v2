#!/usr/bin/python3
""" Place Module for HBNB project """
import od
from sqlalchemy import (String, Column, Integer, Float, ForeignKey)
from models.base_model import BaseModel, Base
import models



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenities = relationship('Amenity', secondary='place_amenities', viewonly=False)
    amenity_ids = []
