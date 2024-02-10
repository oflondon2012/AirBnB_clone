#!/usr/bin/env python3

"""
This module contains the User model test suite
"""

from datetime import datetime
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """
    This class contains the test suite for the User class
    """

    def test_init(self) -> None:
        """
        This method tests the __init__ method of the User class
        """
        u1 = User()
        self.assertIsInstance(u1, User)
        self.assertIsInstance(u1.id, str)
        self.assertIsInstance(u1.created_at, datetime)
        self.assertIsInstance(u1.updated_at, datetime)
        model_json = u1.to_dict()
        self.assertIsInstance(model_json, dict)
        self.assertEqual(model_json["id"], u1.id)
        self.assertEqual(model_json["created_at"], u1.created_at.isoformat())
        self.assertEqual(model_json["updated_at"], u1.updated_at.isoformat())
        self.assertEqual(model_json["__class__"], "User")
        u1m = User(**model_json)
        self.assertIsInstance(u1m, User)
        self.assertEqual(u1m.id, u1.id)
        self.assertEqual(u1m.created_at, u1.created_at)
        self.assertEqual(u1m.updated_at, u1.updated_at)

    def test_email(self) -> None:
        """
        This method tests the email attribute of the User class
        """
        u1 = User()
        self.assertIsInstance(u1.email, str)
        self.assertEqual(u1.email, "")
        u1.email = ""
        self.assertEqual(u1.email, "")
        u1.email = "a"
        self.assertEqual(u1.email, "a")
        u1.email = "abc"
        self.assertEqual(u1.email, "abc")

    def test_password(self) -> None:
        """
        This method tests the password attribute of the User class
        """
        u1 = User()
        self.assertIsInstance(u1.password, str)
        self.assertEqual(u1.password, "")
        u1.password = ""
        self.assertEqual(u1.password, "")
        u1.password = "a"
        self.assertEqual(u1.password, "a")
        u1.password = "abc"
        self.assertEqual(u1.password, "abc")

    def test_first_name(self) -> None:
        """
        This method tests the first_name attribute of the User class
        """
        u1 = User()
        self.assertIsInstance(u1.first_name, str)
        self.assertEqual(u1.first_name, "")
        u1.first_name = ""
        self.assertEqual(u1.first_name, "")
        u1.first_name = "a"
        self.assertEqual(u1.first_name, "a")
        u1.first_name = "abc"
        self.assertEqual(u1.first_name, "abc")

    def test_last_name(self) -> None:
        """
        This method tests the last_name attribute of the User class
        """
        u1 = User()
        self.assertIsInstance(u1.last_name, str)
        self.assertEqual(u1.last_name, "")
        u1.last_name = ""
        self.assertEqual(u1.last_name, "")
        u1.last_name = "a"
        self.assertEqual(u1.last_name, "a")
        u1.last_name = "abc"
        self.assertEqual(u1.last_name, "abc")

    def test_to_dict(self) -> None:
        """
        This method tests the to_dict method of the User class
        """
        u1 = User()
        model_json = u1.to_dict()
        self.assertIsInstance(model_json, dict)
        self.assertEqual(model_json["id"], u1.id)
        self.assertEqual(model_json["created_at"], u1.created_at.isoformat())
        self.assertEqual(model_json["updated_at"], u1.updated_at.isoformat())
        self.assertEqual(model_json["__class__"], "User")

    def test_str(self) -> None:
        """
        This method tests the __str__ method of the User class
        """
        u1 = User()
        self.assertIsInstance(u1.__str__(), str)
        self.assertEqual(str(u1), "[User] ({}) {}".format(u1.id, u1.__dict__))
        u1.email = "a"
        self.assertEqual(str(u1), "[User] ({}) {}".format(u1.id, u1.__dict__))

    def test_save(self) -> None:
        """
        This method tests the save method of the User class
        """
        u1 = User()
        u1.save()
        self.assertNotEqual(u1.created_at, u1.updated_at)

    def test_update(self) -> None:
        """
        This method tests the update method of the User class
        """
        u1 = User()
        u1.save()
        u1m = u1.updated_at
        u1.save()
        self.assertNotEqual(u1m, u1.updated_at)

    def test_type(self) -> None:
        """
        This method tests the type of the User class
        """
        u1 = User()
        self.assertIsInstance(u1, User)
        self.assertIsInstance(u1.id, str)
        self.assertIsInstance(u1.created_at, datetime)
        self.assertIsInstance(u1.updated_at, datetime)
        self.assertIsInstance(u1.email, str)
        self.assertIsInstance(u1.password, str)
        self.assertIsInstance(u1.first_name, str)
        self.assertIsInstance(u1.last_name, str)

    def test_instance(self) -> None:
        """
        This method tests the instance of the User class
        """
        u1 = User()
        self.assertIsInstance(u1, User)
        u2 = User()
        self.assertIsInstance(u2, User)
        self.assertNotEqual(u1.id, u2.id)

    def test_module_docstring(self) -> None:
        """
        This method tests the module docstring
        """
        self.assertTrue(len(User.__doc__) > 1)

    def test_class_docstring(self) -> None:
        """
        This method tests the class docstring
        """
        self.assertTrue(len(User.__doc__) > 1)


if __name__ == "__main__":
    unittest.main()
