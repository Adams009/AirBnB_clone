#!/usr/bin/python3
"""The BaseModel class module."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """"Represents the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Not used.
            **kwargs (dict): key and value
        """
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, format_t)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Update the public instance attribute."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values.

        Include class name to the keys and values.
        """
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        return copy_dict

    def __str__(self):
        """Creating the string method."""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
