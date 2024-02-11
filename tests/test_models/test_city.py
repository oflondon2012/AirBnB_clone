#!/usr/bin/python3

"""
This module contains the test for the City class.
"""

import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class."""

    def test_init(self):
        """Test the initialization of the City class."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method of the City class."""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))

    def test_to_dict(self):
        """Test the to_dict method of the City class."""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)
        self.assertEqual(city_dict["created_at"], city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], city.updated_at.isoformat())

    def test_save(self):
        """Test the save method of the City class."""
        city = City()
        old_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(old_updated_at, city.updated_at)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.created_at, datetime)

    def test_kwargs(self):
        """Test the update method of the City class."""
        city = City()
        city.name = "San Francisco"
        city.save()
        city_dict = city.to_dict()
        city2 = City(**city_dict)
        self.assertEqual(city.name, city2.name)
        self.assertEqual(city.created_at, city2.created_at)
        self.assertEqual(city.updated_at, city2.updated_at)
        self.assertEqual(city.id, city2.id)
        self.assertEqual(city.__class__.__name__, city2.__class__.__name__)
        self.assertNotEqual(city, city2)


if __name__ == "__main__":
    unittest.main()
