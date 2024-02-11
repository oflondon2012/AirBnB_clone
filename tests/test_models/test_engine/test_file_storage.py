#!/usr/bin/python3

"""
This module contains the FileStorage class that serializes instances to a JSON
file and deserializes JSON file to instances
"""

import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up the FileStorage class"""
        self.storage = FileStorage()

    def test_all(self):
        """Test the all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the new method"""
        bm = BaseModel()
        self.storage.new(bm)
        self.assertIn("BaseModel.{}".format(bm.id), self.storage.all().keys())

    def test_save(self):
        """Test the save method"""
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, "r") as f:
            self.assertIn("BaseModel.{}".format(bm.id), json.load(f).keys())

    def test_reload(self):
        """Test the reload method"""
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel.{}".format(bm.id), self.storage.all().keys())
        self.assertIsInstance(
            self.storage.all()["BaseModel.{}".format(bm.id)], BaseModel
        )


if __name__ == "__main__":
    unittest.main()
