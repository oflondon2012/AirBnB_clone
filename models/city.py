#!/usr/bin/env python3

"""
This module contains the City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the City object."""
        super().__init__(*args, **kwargs)