#!/usr/bin/env python3
"""Unittest for User class"""

import unittest
import inspect
import pep8
from datetime import datetime
from models.user import User
import models.user as user_module


class TestUser_docs(unittest.TestCase):
    """Unit tests for checking the documentation and code style of the User class"""

    @classmethod
    def setUpClass(cls):
        """Set up for documentation tests"""
        cls.user_methods = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that 'models/user.py' conforms to PEP 8"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP 8 code style errors in 'user.py'")

    def test_pep8_conformance_test_user(self):
        """Test that 'tests/test_models/test_user.py' conforms to PEP 8"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP 8 code style errors in 'test_user.py'")

    def test_user_module_docstring(self):
        """Test for the docstring in 'user.py' module"""
        self.assertIsNotNone(user_module.__doc__,
                             "'user.py' needs a docstring")
        self.assertGreaterEqual(len(user_module.__doc__),
                                1, "'user.py' docstring is too short")

    def test_user_class_docstring(self):
        """Test for the docstring in the User class"""
        self.assertIsNotNone(User.__doc__, "User User class needs a docstring")
        self.assertGreaterEqual(len(User.__doc__), 1,
                                "User class docstring is too short")

    def test_user_method_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for method_name, method in self.user_methods:
            with self.subTest(method=method_name):
                self.assertIsNotNone(
                    method.__doc__, f"{method_name} method needs a docstring"
                )
                self.assertGreaterEqual(
                    len(method.__doc__), 1,
                    f"{method_name} method docstring is too short")


class TestUser(unittest.TestCase):
    """TestUser class for testring User class"""

    def setUp(self):
        """Set up User for testing"""
        self.user = User()
        self.user.first_name = "youssef"
        self.user.last_name = "bouryal"
        self.user.email = "airbnb_clone@alx.com"
        self.user.password = "1234password"

    def test_user_instance(self):
        """Test user instance"""
        self.assertIsInstance(self.user, User)

    def test_user_email(self):
        """Test user email"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(self.user.email, "airbnb_clone@alx.com")

    def test_user_password(self):
        """Test user password"""
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(self.user.password, "1234password")

    def test_user_first_name(self):
        """Test user first_name"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(self.user.first_name, "youssef")

    def test_user_last_name(self):
        """Test user last_name """
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(type(self.user.last_name), str)
        self.assertEqual(self.user.last_name, "bouryal")

    def test_user_id(self):
        """Test user id"""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertEqual(type(self.user.id), str)

    def test_user_created_at(self):
        """Test user created_at"""
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertEqual(type(self.user.created_at), datetime)

    def test_user_updated_at(self):
        """Test user updated_at"""
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertEqual(type(self.user.updated_at), datetime)

    def test_kwargs(self):
        """Tests user kwargs"""
        user = User(**self.user.to_dict())
        self.assertEqual(self.user.id, user.id)
        self.assertEqual(self.user.created_at, user.created_at)
        self.assertEqual(self.user.updated_at, user.updated_at)
        self.assertNotEqual(self.user, user)


if __name__ == "__main__":
    unittest.main()
