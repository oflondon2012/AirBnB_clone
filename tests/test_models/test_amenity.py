#!/usr/bin/env python3

"""
Unittest for the Amenity class.
"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Unittest for the Amenity class.
    """

    def test_init(self):
        """
        Test the __init__ method.
        """
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(a.created_at, datetime)
        self.assertIsInstance(a.updated_at, datetime)
        model_json = a.to_dict()
        self.assertIsInstance(model_json, dict)
        self.assertEqual(model_json["id"], a.id)
        self.assertEqual(model_json["created_at"], a.created_at.isoformat())
        self.assertEqual(model_json["updated_at"], a.updated_at.isoformat())
        self.assertEqual(model_json["__class__"], "Amenity")
        am = Amenity(**model_json)
        self.assertIsInstance(am, Amenity)
        self.assertEqual(am.id, a.id)
        self.assertEqual(am.created_at, a.created_at)
        self.assertEqual(am.updated_at, a.updated_at)

    def test_str(self):
        """
        Test the __str__ method.
        """
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertIsInstance(a.__str__(), str)
        self.assertEqual(a.__str__(), f"[Amenity] ({a.id}) {a.__dict__}")
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(a.created_at, datetime)
        self.assertIsInstance(a.updated_at, datetime)

    def test_save(self):
        """
        Test the save method.
        """
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(a.created_at, datetime)
        self.assertIsInstance(a.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
