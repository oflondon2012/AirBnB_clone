#!/usr/bin/env python3

"""
This module contains some unique instances for the application
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

storage = FileStorage()
storage.reload()

available_models = {"BaseModel": BaseModel, "User": User}
