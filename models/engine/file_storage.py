#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        if cls is None
            Returns a dictionary of models currently in storage
        else
            return a filtered dict
        """
        if cls:
            temp = {k: v for k, v in self.__objects.items()
                    if type(v).__name__ == cls}
            return temp
        return (self.__objects)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """deletes obj from __object private class attr"""
        if obj:
            className = obj.__str__().split("[")[1].split("]")[0]
            classId = obj.__str__().split("(")[1].split(")")[0]
            del FileStorage.__objects["{}.{}".format(className, classId)]

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.__objects[key] = models.classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
