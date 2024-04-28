#!/usr/bin/env python3
""" BaseModel test suit

Unittest classes:
    TestBase_instantiation
    TestBase_save
    TestBase_to_dict
    TestBase_str
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase_instantiation(unittest.TestCase):
    """Unittests of instantiation of the BaseModel class"""
    def test_with_args(self):
        x = BaseModel("foobar", "foo", "bar")
        self.assertNotEqual(x.id, "foobar")

    def test_with_kwargs(self):
        kwargs = {
                "id": "youssefbouryal",
                "created_at": "2023-10-10T08:08:59.234200",
                "updated_at": "2023-10-10T08:08:59.234200",
                }
        x = BaseModel(**kwargs)
        self.assertEqual(x.id, "youssefbouryal")
        self.assertIs(type(x.created_at), datetime)
        self.assertIs(type(x.updated_at), datetime)

    def test_with_new_vars(self):
        kwargs = {
                "name": "Youssef",
                "number": 10,
                "id": "youssefbouryal",
                "created_at": "2023-10-10T08:08:59.234200",
                "updated_at": "2023-10-10T08:08:59.234200",
                }
        x = BaseModel(**kwargs)
        self.assertEqual(x.name, "Youssef")


class TestBase_str(unittest.TestCase):
    """Unittests of str method of BaseModel class"""

    def test_return_type(self):
        x = BaseModel()
        self.assertIs(str, type(x.__str__()))

    def test_str_with_two_instance(self):
        x = BaseModel()
        x.name = "John"
        kwargs = x.to_dict().copy()
        y = BaseModel(**kwargs)
        self.assertEqual(len(str(x)), len(str(y)))


class TestBase_save(unittest.TestCase):
    """Unittests of save method"""

    def test_save(self):
        x = BaseModel()
        x_dict = x.to_dict().copy()
        x.save()
        x_saved_dict = x.to_dict().copy()
        self.assertNotEqual(x_dict, x_saved_dict)


class TestBase_to_dict(unittest.TestCase):
    """Unittests of to_dict method"""

    def test_to_dict_return_type(self):
        x = BaseModel()
        self.assertIs(type(x.to_dict()), dict)

    def test_to_dict_length(self):
        x = BaseModel()
        x.name = "BaseModel"
        _dict = x.to_dict()
        self.assertEqual(len(_dict), 5)

    def test_to_dict_with_str(self):
        x = BaseModel()
        x.name = "BaseModel"
        self.assertNotEqual(x.to_dict(), x.__dict__)

    def test_to_dict_with_kwargs(self):
        kwargs = {
                "name": "Youssef",
                "number": 10,
                "id": "youssefbouryal",
                "created_at": "2023-10-10T08:08:59.234200",
                "updated_at": "2023-10-10T08:08:59.234200",
                }
        _dict = {
                "name": "Youssef",
                "number": 10,
                "id": "youssefbouryal",
                "created_at": "2023-10-10T08:08:59.234200",
                "updated_at": "2023-10-10T08:08:59.234200",
                "__class__": "BaseModel",
                }
        x = BaseModel(**kwargs)
        self.assertEqual(x.to_dict(), _dict)


if __name__ == "__main__":
    unittest.main()
