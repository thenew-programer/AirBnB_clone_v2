#!/usr/bin/python3
"""Unittest for State class"""

import unittest
import inspect
import pep8
from models.state import State
import models.state as state_module


class TestState_docs(unittest.TestCase):
    """Unit tests for checking the documentation and code
    style of the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up for documentation tests"""
        cls.state_methods = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """Test that 'models/state.py' conforms to PEP 8"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP 8 code style errors in 'state.py'")

    def test_state_module_docstring(self):
        """Test for the docstring in 'state.py' module"""
        self.assertIsNotNone(state_module.__doc__,
                             "'state.py' needs a docstring")
        self.assertGreaterEqual(len(state_module.__doc__),
                                1, "'state.py' docstring is too short")

    def test_state_class_docstring(self):
        """Test for the docstring in the State class"""
        self.assertIsNotNone(State.__doc__, "State class needs a docstring")
        self.assertGreaterEqual(len(State.__doc__), 1,
                                "State class docstring is too short")

    def test_state_method_docstrings(self):
        """Test for the presence of docstrings in State methods"""
        for method_name, method in self.state_methods:
            with self.subTest(method=method_name):
                self.assertIsNotNone(
                    method.__doc__, f"{method_name} method needs a docstring"
                )
                self.assertGreaterEqual(
                    len(method.__doc__), 1,
                    f"{method_name} method docstring is too short")


class TestState(unittest.TestCase):
    """Test cases for TestState Class"""

    def setUp(self):
        """Sets up State for testing"""
        self.state = State()
        self.state.name = "hello"

    def tearDown(self):
        """Tears down State testing"""
        del self.state

    def test_state__isinstance(self):
        """Tests state instance"""
        self.assertIsInstance(self.state, State)

    def test_state_attr_name(self):
        """Tests state name"""
        self.assertTrue(hasattr(self.state, "name"))
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
