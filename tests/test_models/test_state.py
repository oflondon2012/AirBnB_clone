#!/usr/bin/env python3

"""
This module contains the test for the State class.
"""

import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """Test the State class."""

    def test_init(self):
        """Test the initialization of the State class."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method of the State class."""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))

    def test_to_dict(self):
        """Test the to_dict method of the State class."""
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)
        self.assertEqual(
            state_dict["created_at"], state.created_at.isoformat()
        )
        self.assertEqual(
            state_dict["updated_at"], state.updated_at.isoformat()
        )

    def test_save(self):
        """Test the save method of the State class."""
        state = State()
        old_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(old_updated_at, state.updated_at)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.created_at, datetime)

    def test_kwargs(self):
        """Test the update method of the State class."""
        state = State()
        state.name = "California"
        state.save()
        state_dict = state.to_dict()
        state2 = State(**state_dict)
        self.assertEqual(state.name, state2.name)
        self.assertEqual(state.created_at, state2.created_at)
        self.assertEqual(state.updated_at, state2.updated_at)
        self.assertEqual(state.id, state2.id)
        self.assertEqual(state.__class__.__name__, state2.__class__.__name__)
        self.assertNotEqual(state, state2)
        self.assertIsNot(state, state2)

    def test_type(self):
        """Test the type of the State class."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
