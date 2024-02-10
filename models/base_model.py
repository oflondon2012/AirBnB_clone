#!/usr/bin/env python3

"""
This module contains the base model class
- BaseModel: the base model class
- Public instance attributes:
  - id: string - assign with an uuid when an instance is created
  - created_at: datetime - assign with the current datetime when an
    instance is created
  - updated_at: datetime - assign with the current datetime when an
    instance is created and it will be updated every time you change your
    object
- __str__: should print: [<class name>] (<self.id>) <self.__dict__>
- Public instance methods:
  - save(self): updates the public instance attribute updated_at with
    the current datetime
  - to_dict(self): returns a dictionary containing all keys/values of
    __dict__ of the instance
"""

import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class"""

    def __init__(self, **kwargs):
        """Initializes the BaseModel class"""
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self) -> None:
        """Updates the public instance attribute updated_at with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def __str__(self) -> str:
        """Returns a string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
