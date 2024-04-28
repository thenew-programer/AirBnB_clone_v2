#!/usr/bin/python3
"""Defines unittests for Review class.

Unittest classes:
    TestReview_docs
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import unittest
import inspect
import pep8
import models
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_docs(unittest.TestCase):
    """Unit tests for checking documentation and code style of the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the documentation tests"""
        cls.review_methods = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Test that 'models/review.py' conforms to PEP 8"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP 8 code style errors in 'review.py'")

    def test_pep8_conformance_test_review(self):
        """Test that 'tests/test_models/test_review.py' conforms to PEP 8"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP 8 code style errors in 'test_review.py'")

    def test_review_module_docstring(self):
        """Test for the docstring in 'models/review.py'"""
        self.assertIsNotNone(models.review.__doc__,
                             "'review.py' needs a docstring")
        self.assertGreaterEqual(
            len(models.review.__doc__), 1, "'review.py' docstring is too short")

    def test_review_class_docstring(self):
        """Test for the docstring in the Review class"""
        self.assertIsNotNone(Review.__doc__, "Review class needs a docstring")
        self.assertGreaterEqual(len(Review.__doc__), 1,
                                "Review class docstring is too short")

    def test_review_method_docstrings(self):
        """Test for the presence of docstrings in Review methods"""
        for method_name, method in self.review_methods:
            with self.subTest(method=method_name):
                self.assertIsNotNone(
                    method.__doc__, f"{method_name} method needs a docstring"
                )
                self.assertGreaterEqual(
                    len(method.__doc__), 1,
                    f"{method_name} method docstring is too short")


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_two_reviews_different_created_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_reviews_different_updated_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_args_unused(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
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

    def test_one_save(self):
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        self.assertLess(first_updated_at, rv.updated_at)

    def test_two_saves(self):
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        second_updated_at = rv.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rv.save()
        self.assertLess(second_updated_at, rv.updated_at)

    def test_save_with_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    def test_save_updates_file(self):
        rv = Review()
        rv.save()
        rvid = "Review." + rv.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())

    def test_to_dict_contains_added_attributes(self):
        rv = Review()
        rv.middle_name = "Alx"
        rv.my_number = 98
        self.assertEqual("Alx", rv.middle_name)
        self.assertIn("my_number", rv.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        rv = Review()
        rv.id = "000000"
        rv.created_at = rv.updated_at = dt
        tdict = {
            "id": "000000",
            "__class__": "Review",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(rv.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        rv = Review()
        self.assertNotEqual(rv.to_dict(), rv.__dict__)

    def test_to_dict_with_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)


if __name__ == "__main__":
    unittest.main()
