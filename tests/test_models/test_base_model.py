#!/usr/bin/env python3
""" BaseModel test suit

Unittest classes:
    TestBase_docs
    TestBase_instantiation
    TestBase_save
    TestBase_to_dict
    TestBase_str
"""
import unittest
import inspect
from datetime import datetime
import pep8
from models import base_model
BaseModel = base_model.BaseModel
base_model_docs__ = base_model.__doc__


class TestBaseModel_docs(unittest.TestCase):
    """Unit tests for checking documentation and code style in BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.base_methods = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py and related test files conform to PEP 8"""
        file_paths = ['models/base_model.py',
                      'tests/test_models/test_base_model.py']
        pep8_checker = pep8.StyleGuide(quiet=True)

        for path in file_paths:
            with self.subTest(path=path):
                errors = pep8_checker.check_files([path]).total_errors
                self.assertEqual(
                    errors, 0, f"PEP 8 code style errors in '{path}'")

    def test_module_docstring(self):
        """Test for the existence of module docstring in base_model.py"""
        self.assertIsNotNone(base_model.__doc__,
                             "base_model.py needs a docstring")
        self.assertGreater(len(base_model.__doc__), 1,
                           "base_model.py docstring is too short")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNotNone(
            BaseModel.__doc__, "BaseModel class needs a docstring")
        self.assertGreaterEqual(len(BaseModel.__doc__),
                                1, "BaseModel class docstring is too short")

    def test_method_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for method_name, method in self.base_methods:
            with self.subTest(method=method_name):
                self.assertIsNotNone(
                    method.__doc__, f"{method_name} method needs a docstring"
                )
                self.assertGreater(
                    len(method.__doc__), 1,
                    f"{method_name} method docstring is too short")


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
