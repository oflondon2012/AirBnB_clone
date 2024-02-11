#!/usr/bin/python3

"""
This module contains the test for the Review class.
"""

import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test the Review class."""

    def test_init(self):
        """Test the initialization of the Review class."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method of the Review class."""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))

    def test_to_dict(self):
        """Test the to_dict method of the Review class."""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)
        self.assertEqual(
            review_dict["created_at"], review.created_at.isoformat()
        )
        self.assertEqual(
            review_dict["updated_at"], review.updated_at.isoformat()
        )

    def test_save(self):
        """Test the save method of the Review class."""
        review = Review()
        old_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(old_updated_at, review.updated_at)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsInstance(review.created_at, datetime)

    def test_kwargs(self):
        """Test the update method of the Review class."""
        review = Review()
        review.text = "Great place"
        review.save()
        review_dict = review.to_dict()
        review2 = Review(**review_dict)
        self.assertEqual(review.text, review2.text)
        self.assertEqual(review.created_at, review2.created_at)
        self.assertEqual(review.updated_at, review2.updated_at)
        self.assertEqual(review.id, review2.id)
        self.assertEqual(review.__class__.__name__, review2.__class__.__name__)


if __name__ == "__main__":
    unittest.main()
