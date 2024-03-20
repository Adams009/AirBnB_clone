#!/usr/bin/python3
"""Module file_storage

The Module of FileStorage Class
"""


import importlib
import json
import os
import re


class FileStorage:
    """FileStorage Class

    Attributes:
        __file_path (str): path to JSON file
        __objects (dict): A dictionary of objects.

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file"""
        if (os.path.isfile(self.__file_path)
                and os.path.getsize(self.__file_path) > 0):
            with open(self.__file_path, 'r') as f:
                self.__objects = {k: self.get_class(k.split(".")[0])(**v)
                                  for k, v in json.load(f).items()}

    def get_class(self, name):
        """ returns a class from models"""
        sub_module = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
        module = importlib.import_module(f"models.{sub_module}")
        return getattr(module, name)
