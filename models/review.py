#!/usr/bin/python3

"""
This module contains the Review class, which inherits from BaseModel.
Public class attributes:
    place_id: string - empty string
    user_id: string - empty string
    text: string - empty string
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Review object."""
        super().__init__(*args, **kwargs)
