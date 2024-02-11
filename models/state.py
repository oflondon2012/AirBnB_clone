#!/usr/bin/python3

"""
This module contains the State class, which inherits from BaseModel.
Public class attributes:
    name: string - empty string
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the State object."""
        super().__init__(*args, **kwargs)
