#!/usr/bin/python3
"""Defines unittests for City class.

Unittest classes:
    TestCity_docs
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
from datetime import datetime
from time import sleep
import pep8
import inspect
import unittest
import models
from models.city import City


class TestCity_docs(unittest.TestCase):
    """Unit tests to check the documentation and code style of the City class
    """

    @classmethod
    def setUpClass(cls):
        """Set up for documentation tests"""
        cls.city_methods = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that 'models/city.py' conforms to PEP 8"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style issues in 'city.py'")

    def test_city_module_docstring(self):
        """Test for the docstring in 'city.py' module"""
        self.assertIsNotNone(models.city.__doc__,
                             "'city.py' needs a docstring")
        self.assertGreaterEqual(len(models.city.__doc__),
                                1, "'city.py' docstring is too short")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNotNone(City.__doc__, "City class needs a docstring")
        self.assertGreaterEqual(len(City.__doc__), 1,
                                "City class docstring is too short")

    def test_city_method_docstrings(self):
        """Test for the presence of docstrings in City methods"""
        for method_name, method in self.city_methods:
            with self.subTest(method=method_name):
                self.assertIsNotNone(
                    method.__doc__, f"{method_name} method needs a docstring"
                )
                self.assertGreater(
                    len(method.__doc__), 1,
                    f"{method_name} method docstring is too short")


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        city = City()
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_name_is_public_class_attribute(self):
        city = City()
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_two_cities_unique_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        cystr = city.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method."""

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save_updates_file(self):
        city = City()
        city.save()
        cyid = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        city = City()
        city.middle_name = "Holberton"
        city.my_number = 98
        self.assertEqual("Holberton", city.middle_name)
        self.assertIn("my_number", city.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        city = City()
        cy_dict = city.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_to_dict_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
