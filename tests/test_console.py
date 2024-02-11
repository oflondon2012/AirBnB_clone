#!/usr/bin/python3
"""
This module contains the tests for the console module.
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """Test the console module."""

    def setUp(self):
        """Set up the tests."""
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        """Clean up after each test."""
        self.console = None
        self.mock_stdout.close()

    def test_create(self):
        """Test the create command."""
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("create BaseModel")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.assertTrue(
                isinstance(
                    storage.all()[
                        "BaseModel." + self.mock_stdout.getvalue().strip()
                    ],
                    BaseModel,
                )
            )
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("create User")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.assertTrue(
                isinstance(
                    storage.all()[
                        "User." + self.mock_stdout.getvalue().strip()
                    ],
                    User,
                )
            )
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("create State")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.assertTrue(
                isinstance(
                    storage.all()[
                        "State." + self.mock_stdout.getvalue().strip()
                    ],
                    State,
                )
            )
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("create City")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.assertTrue(
                isinstance(
                    storage.all()[
                        "City." + self.mock_stdout.getvalue().strip()
                    ],
                    City,
                )
            )
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("create Amenity")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.assertTrue(
                isinstance(
                    storage.all()[
                        "Amenity." + self.mock_stdout.getvalue().strip()
                    ],
                    Amenity,
                )
            )
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("create Place")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.assertTrue(
                isinstance(
                    storage.all()[
                        "Place." + self.mock_stdout.getvalue().strip()
                    ],
                    Place,
                )
            )
            self.mock_stdout.seek(0)
            self.mock_stdout
            self.mock_stdout.truncate(0)
            self.console.onecmd("create Review")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.assertTrue(
                isinstance(
                    storage.all()[
                        "Review." + self.mock_stdout.getvalue().strip()
                    ],
                    Review,
                )
            )
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)

    def test_show(self):
        """Test the show command."""
        b = BaseModel()
        b.save()
        u = User()
        u.save()
        s = State()
        s.save()
        c = City()
        c.save()
        a = Amenity()
        a.save()
        p = Place()
        p.save()
        r = Review()
        r.save()
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("show BaseModel " + b.id)
            self.assertEqual(self.mock_stdout.getvalue().strip(), str(b))
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("show User " + u.id)
            self.assertEqual(self.mock_stdout.getvalue().strip(), str(u))
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("show State " + s.id)
            self.assertEqual(self.mock_stdout.getvalue().strip(), str(s))
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("show City " + c.id)
            self.assertEqual(self.mock_stdout.getvalue().strip(), str(c))
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("show Amenity " + a.id)
            self.assertEqual(self.mock_stdout.getvalue().strip(), str(a))
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("show Place " + p.id)
            self.assertEqual(self.mock_stdout.getvalue().strip(), str(p))
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("show Review " + r.id)
            self.assertEqual(self.mock_stdout.getvalue().strip(), str(r))
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)

    def test_destroy(self):
        """Test the destroy command."""
        b = BaseModel()
        b.save()
        u = User()
        u.save()
        s = State()
        s.save()
        c = City()
        c.save()
        a = Amenity()
        a.save()
        p = Place()
        p.save()
        r = Review()
        r.save()
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("destroy BaseModel " + b.id)
            self.assertTrue(storage.all().get("BaseModel." + b.id) is None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("destroy User " + u.id)
            self.assertTrue(storage.all().get("User." + u.id) is None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("destroy State " + s.id)
            self.assertTrue(storage.all().get("State." + s.id) is None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("destroy City " + c.id)
            self.assertTrue(storage.all().get("City." + c.id) is None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("destroy Amenity " + a.id)
            self.assertTrue(storage.all().get("Amenity." + a.id) is None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("destroy Place " + p.id)
            self.assertTrue(storage.all().get("Place." + p.id) is None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("destroy Review " + r.id)
            self.assertTrue(storage.all().get("Review." + r.id) is None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)

    def test_all(self):
        """Test the all command."""
        b = BaseModel()
        b.save()
        u = User()
        u.save()
        s = State()
        s.save()
        c = City()
        c.save()
        a = Amenity()
        a.save()
        p = Place()
        p.save()
        r = Review()
        r.save()
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("all BaseModel")
            self.assertIn(str(b), self.mock_stdout.getvalue())
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("all User")
            self.assertIn(str(u), self.mock_stdout.getvalue())
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("all State")
            self.assertIn(str(s), self.mock_stdout.getvalue())
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("all City")
            self.assertIn(str(c), self.mock_stdout.getvalue())
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("all Amenity")
            self.assertIn(str(a), self.mock_stdout.getvalue())
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("all Place")
            self.assertIn(str(p), self.mock_stdout.getvalue())
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("all Review")
            self.assertIn(str(r), self.mock_stdout.getvalue())
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)

    def test_update(self):
        """Test the update command."""
        b = BaseModel()
        b.save()
        u = User()
        u.save()
        s = State()
        s.save()
        c = City()
        c.save()
        a = Amenity()
        a.save()
        p = Place()
        p.save()
        r = Review()
        r.save()
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd(
                "update BaseModel " + b.id + ' name "Holberton"'
            )
            self.assertEqual(b.name, "Holberton")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("update User " + u.id + ' name "Betty"')
            self.assertEqual(u.name, "Betty")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("update State " + s.id + ' name "California"')
            self.assertEqual(s.name, "California")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd(
                "update City " + c.id + ' name "San Francisco"'
            )
            self.assertEqual(c.name, "San Francisco")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("update Amenity " + a.id + ' name "Wifi"')
            self.assertEqual(a.name, "Wifi")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("update Place " + p.id + ' name "House"')
            self.assertEqual(p.name, "House")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("update Review " + r.id + ' text "Great"')
            self.assertEqual(r.text, "Great")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)

    def test_count(self):
        """Test the count command."""
        b = BaseModel()
        b.save()
        u = User()
        u.save()
        s = State()
        s.save()
        c = City()
        c.save()
        a = Amenity()
        a.save()
        p = Place()
        p.save()
        r = Review()
        r.save()
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("BaseModel.count()")
            self.assertEqual(self.mock_stdout.getvalue().strip(), "2")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("User.count()")
            self.assertEqual(self.mock_stdout.getvalue().strip(), "2")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("State.count()")
            self.assertEqual(self.mock_stdout.getvalue().strip(), "2")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("City.count()")
            self.assertEqual(self.mock_stdout.getvalue().strip(), "2")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("Amenity.count()")
            self.assertEqual(self.mock_stdout.getvalue().strip(), "2")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("Place.count()")
            self.assertEqual(self.mock_stdout.getvalue().strip(), "2")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("Review.count()")
            self.assertEqual(self.mock_stdout.getvalue().strip(), "2")
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)

    def test_help(self):
        """Test the help command."""
        with patch("sys.stdout", new=self.mock_stdout):
            self.console.onecmd("help")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("help quit")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("help create")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("help show")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("help destroy")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("help all")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("help update")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)
            self.console.onecmd("help count")
            self.assertTrue(self.mock_stdout.getvalue() != "")
            self.assertTrue(self.mock_stdout.getvalue() is not None)
            self.mock_stdout.seek(0)
            self.mock_stdout.truncate(0)

    def test_emptyline(self):
        """Test the emptyline method."""
        with patch("sys.stdout", new=self.mock_stdout):
            self.assertTrue(self.console.onecmd("") is None)

    def test_EOF(self):
        """Test the EOF method."""
        with patch("sys.stdout", new=self.mock_stdout):
            self.assertTrue(self.console.onecmd("EOF") is True)

    def test_quit(self):
        """Test the quit method."""
        with patch("sys.stdout", new=self.mock_stdout):
            self.assertTrue(self.console.onecmd("quit") is True)


if __name__ == "__main__":
    unittest.main()
