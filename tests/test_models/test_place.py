#!/usr/bin/python3

"""
Unittest for the Place class.
"""

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    Unittest for the Place class.
    """

    def test_init(self):
        """
        Test the __init__ method.
        """
        p = Place()
        self.assertIsInstance(p, Place)
        self.assertIsInstance(p.id, str)
        self.assertIsInstance(p.created_at, datetime)
        self.assertIsInstance(p.updated_at, datetime)
        model_json = p.to_dict()
        self.assertIsInstance(model_json, dict)
        self.assertEqual(model_json["id"], p.id)
        self.assertEqual(model_json["created_at"], p.created_at.isoformat())
        self.assertEqual(model_json["updated_at"], p.updated_at.isoformat())
        self.assertEqual(model_json["__class__"], "Place")
        pl = Place(**model_json)
        self.assertIsInstance(pl, Place)
        self.assertEqual(pl.id, p.id)
        self.assertEqual(pl.created_at, p.created_at)
        self.assertEqual(pl.updated_at, p.updated_at)

    def test_str(self):
        """
        Test the __str__ method.
        """
        p = Place()
        self.assertIsInstance(p, Place)
        self.assertIsInstance(p.__str__(), str)
        self.assertEqual(p.__str__(), f"[Place] ({p.id}) {p.__dict__}")
        self.assertIsInstance(p.id, str)
        self.assertIsInstance(p.created_at, datetime)
        self.assertIsInstance(p.updated_at, datetime)

    def test_save(self):
        """
        Test the save method.
        """
        p = Place()
        self.assertIsInstance(p, Place)
        self.assertIsInstance(p.id, str)
        self.assertIsInstance(p.created_at, datetime)
        self.assertIsInstance(p.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
