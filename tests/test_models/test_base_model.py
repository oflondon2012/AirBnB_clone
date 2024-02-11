#!/usr/bin/python3

"""
This module contains the tests for the base_model module
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    This class contains the tests for the BaseModel class
    """

    def test_init(self) -> None:
        """
        This method tests the __init__ method of the BaseModel class
        """
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)
        model_json = b1.to_dict()
        self.assertIsInstance(model_json, dict)
        self.assertEqual(model_json["id"], b1.id)
        self.assertEqual(model_json["created_at"], b1.created_at.isoformat())
        self.assertEqual(model_json["updated_at"], b1.updated_at.isoformat())
        self.assertEqual(model_json["__class__"], "BaseModel")
        b1m = BaseModel(**model_json)
        self.assertIsInstance(b1m, BaseModel)
        self.assertEqual(b1m.id, b1.id)
        self.assertEqual(b1m.created_at, b1.created_at)
        self.assertEqual(b1m.updated_at, b1.updated_at)

    def test_str(self) -> None:
        """
        This method tests the __str__ method of the BaseModel class
        """
        b2 = BaseModel()
        self.assertIsInstance(b2, BaseModel)
        self.assertIsInstance(b2.__str__(), str)
        self.assertEqual(b2.__str__(), f"[BaseModel] ({b2.id}) {b2.__dict__}")
        self.assertIsInstance(b2.id, str)
        self.assertIsInstance(b2.created_at, datetime)
        self.assertIsInstance(b2.updated_at, datetime)

    def test_save(self) -> None:
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

    def test_to_dict(self) -> None:
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

    def test_storage(self) -> None:
        """
        This method tests the storage attribute of the BaseModel class
        """
        b5 = BaseModel()
        self.assertIsInstance(b5, BaseModel)
        self.assertIsInstance(b5.id, str)
        self.assertIsInstance(b5.created_at, datetime)
        self.assertIsInstance(b5.updated_at, datetime)
        self.assertIsInstance(storage.all(), dict)
        self.assertIn(f"BaseModel.{b5.id}", storage.all().keys())
        self.assertEqual(b5, storage.all()[f"BaseModel.{b5.id}"])
        b5.save()
        self.assertIsInstance(storage.all(), dict)
        self.assertIn(f"BaseModel.{b5.id}", storage.all().keys())
        self.assertEqual(b5, storage.all()[f"BaseModel.{b5.id}"])
        b5d = b5.to_dict()
        self.assertIsInstance(b5d, dict)
        self.assertEqual(b5d["id"], b5.id)
        self.assertEqual(b5d["created_at"], b5.created_at.isoformat())
        self.assertEqual(b5d["updated_at"], b5.updated_at.isoformat())
        self.assertEqual(b5d["__class__"], "BaseModel")
        b5.save()
        self.assertIsInstance(storage.all(), dict)

    def test_kwargs(self) -> None:
        """
        This method tests the kwargs argument of the BaseModel class
        """
        b6 = BaseModel()
        self.assertIsInstance(b6, BaseModel)
        self.assertIsInstance(b6.id, str)
        self.assertIsInstance(b6.created_at, datetime)
        self.assertIsInstance(b6.updated_at, datetime)
        b6d = b6.to_dict()
        self.assertIsInstance(b6d, dict)
        b6m = BaseModel(**b6d)
        self.assertIsInstance(b6m, BaseModel)
        self.assertEqual(b6.id, b6m.id)
        self.assertEqual(b6.created_at, b6m.created_at)
        self.assertEqual(b6.updated_at, b6m.updated_at)
        self.assertNotEqual(b6, b6m)
        self.assertIsNot(b6, b6m)
        self.assertIsInstance(b6m.id, str)
        self.assertIsInstance(b6m.created_at, datetime)
        self.assertIsInstance(b6m.updated_at, datetime)

    def test_type(self) -> None:
        """
        This method tests the type of the BaseModel class
        """
        b7 = BaseModel()
        self.assertIsInstance(b7, BaseModel)
        self.assertIsInstance(b7.id, str)
        self.assertIsInstance(b7.created_at, datetime)
        self.assertIsInstance(b7.updated_at, datetime)
        self.assertIsInstance(b7.id, str)
        self.assertIsInstance(b7.created_at, datetime)
        self.assertIsInstance(b7.updated_at, datetime)
        self.assertIsInstance(b7.to_dict(), dict)
        self.assertIsInstance(b7.to_dict()["id"], str)
        self.assertIsInstance(b7.to_dict()["created_at"], str)
        self.assertIsInstance(b7.to_dict()["updated_at"], str)
        self.assertIsInstance(b7.to_dict()["__class__"], str)
        self.assertEqual(b7.to_dict()["__class__"], "BaseModel")
        self.assertIsInstance(b7.__str__(), str)
        self.assertIsInstance(b7.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
