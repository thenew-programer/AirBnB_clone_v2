#!/usr/bin/python3
"""Defines unittests for Amenity.

Unittest classes:
    TestAmenity_docs
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""

import os
import unittest
import inspect
from datetime import datetime
from time import sleep
import pep8
import models
from models.amenity import Amenity


class TestAmenity_docs(unittest.TestCase):
    """Unit tests for checking documentation and code style in Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_methods = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test that 'models/amenity.py' conforms to PEP 8"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP 8 code style errors in 'amenity.py'.")

    def test_amenity_module_docstring(self):
        """Test for the docstring in 'amenity.py' module"""
        self.assertIsNotNone(
            models.amenity.__doc__, "Add a docstring to 'amenity.py'")
        self.assertGreaterEqual(len(models.amenity.__doc__), 1,
                                "Add a longer docstring to 'amenity.py'")

    def test_amenity_class_docstring(self):
        """Test for the docstring in the 'Amenity' class"""
        self.assertIsNotNone(
            Amenity.__doc__, "Add a docstring to 'Amenity' class")
        self.assertGreaterEqual(len(Amenity.__doc__), 1,
                                "Add a longer docstring to 'Amenity' class")

    def test_amenity_method_docstrings(self):
        """Test for the presence of docstrings in 'Amenity' methods"""
        for method in self.amenity_methods:
            self.assertIsNotNone(method[1].__doc__,
                                 f"{method[0]} method needs a docstring")
            self.assertGreaterEqual(len(method[1].__doc__), 1,
                                    f"{method[0]} method needs a longer docstring")


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amenity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenity.__dict__)

    def test_two_amenities_unique_ids(self):
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_two_amenities_different_created_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.created_at, amenity_2.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.updated_at, amenity_2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        amstr = amenity.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, dt)
        self.assertEqual(amenity.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
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
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_save_updates_file(self):
        amenity = Amenity()
        amenity.save()
        amid = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amenity = Amenity()
        amenity.middle_name = "Holberton"
        amenity.my_number = 98
        self.assertEqual("Holberton", amenity.middle_name)
        self.assertIn("my_number", amenity.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amenity = Amenity()
        am_dict = amenity.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "Amenity",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(amenity.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        amenity = Amenity()
        self.assertNotEqual(amenity.to_dict(), amenity.__dict__)

    def test_to_dict_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
