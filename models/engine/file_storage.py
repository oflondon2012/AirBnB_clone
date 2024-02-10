#!/usr/bin/env python3

"""
This module contains the FileStorage class that serializes instances to a JSON
file and deserializes JSON file to instances
"""

import json


class FileStorage:
    """The FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self) -> None:
        """Initializes the FileStorage class"""
        pass

    def all(self) -> dict:
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj) -> None:
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self) -> None:
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f, indent=4)

    def reload(self) -> None:
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
            for _, value in new_dict.items():
                class_name = value["__class__"]
                del value["__class__"]
                self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
