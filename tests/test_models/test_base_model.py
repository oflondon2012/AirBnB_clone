#!/usr/bin/env python3
"""
This module contains the tests for the base_model module
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    This class contains the tests for the BaseModel class
    """

    def test_init(self):
        """
        This method tests the __init__ method of the BaseModel class
        """
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

    def test_str(self):
        """
        This method tests the __str__ method of the BaseModel class
        """
        b2 = BaseModel()
        self.assertIsInstance(b2, BaseModel)
        self.assertIsInstance(b2.__str__(), str)
        self.assertEqual(
            b2.__str__(), f"[BaseModel] ({b2.id}) <{b2.__dict__}>")
        self.assertIsInstance(b2.id, str)
        self.assertIsInstance(b2.created_at, datetime)
        self.assertIsInstance(b2.updated_at, datetime)

    def test_save(self):
        """
        This method tests the save method of the BaseModel class
        """
        b3 = BaseModel()
        self.assertIsInstance(b3, BaseModel)
        self.assertIsInstance(b3.id, str)
        self.assertIsInstance(b3.created_at, datetime)
        self.assertIsInstance(b3.updated_at, datetime)
        i1 = b3.updated_at
        b3.save()
        self.assertIsInstance(b3.updated_at, datetime)
        self.assertNotEqual(b3.updated_at, i1)

    def test_to_dict(self):
        """
        This method tests the to_dict method of the BaseModel class
        """
        b4 = BaseModel()
        self.assertIsInstance(b4, BaseModel)
        self.assertIsInstance(b4.id, str)
        self.assertIsInstance(b4.created_at, datetime)
        self.assertIsInstance(b4.updated_at, datetime)
        d1 = b4.to_dict()
        self.assertIsInstance(d1, dict)
        self.assertEqual(d1["id"], b4.id)
        self.assertEqual(d1["created_at"], b4.created_at.isoformat())
        self.assertEqual(d1["updated_at"], b4.updated_at.isoformat())
        self.assertEqual(d1["__class__"], "BaseModel")
