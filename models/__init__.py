#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""

import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    "City": City,
    "Place": Place,
    "Review": Review,
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "State": State,
    "User": User,
}

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
