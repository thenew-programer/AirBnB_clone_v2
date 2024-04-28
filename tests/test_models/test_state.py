#!/usr/bin/python3
"""Unittest for State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for TestState Class"""

    def setUp(self):
        """Sets up State for testing"""
        self.state = State()

    def tearDown(self):
        """Tears down State testing"""
        del self.state

    def test_state__isinstance(self):
        """Tests state instance"""
        self.assertIsInstance(self.state, State)

    def test_state_attr_name(self):
        """Tests state name"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")
        self.assertEqual(type(self.state.name), str)

    def test_state_attr_id(self):
        """Tests state id"""
        self.assertTrue(hasattr(self.state, "id"))
        self.assertEqual(type(self.state.id), str)

    def test_state_attr_created_at(self):
        """Tests state created_at"""
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertEqual(type(self.state.created_at).__name__, "datetime")

    def test_state_attr_updated_at(self):
        """Tests state updated_at"""
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertEqual(type(self.state.updated_at).__name__, "datetime")

    def test_state_method_str(self):
        """Tests state __str__"""
        self.assertEqual(type(self.state.__str__()), str)

    def test_state_method_save(self):
        """Tests state save"""
        self.state.save()
        self.assertEqual(type(self.state.updated_at).__name__, "datetime")

    def test_state_method_to_dict(self):
        """Tests state to_dict"""
        self.assertEqual(type(self.state.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()

