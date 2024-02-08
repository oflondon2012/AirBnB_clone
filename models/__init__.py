#!/usr/bin/env python3

"""
This module contains some unique instances for the application
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
