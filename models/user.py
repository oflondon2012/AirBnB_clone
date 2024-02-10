#!/usr/bin/env python3

"""
This module contains the User model
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor for User class
        """
        super().__init__(*args, **kwargs)
