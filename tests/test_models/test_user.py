#!/usr/bin/env python3
"""Unittest for User class"""
import unittest
from datetime import datetime
from models.user import User


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

