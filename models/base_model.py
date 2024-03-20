#!/usr/bin/python3
"""Module base_model

The Module of BaseModel Class
"""

import uuid
from datetime import datetime

import models


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """method & instantiation of Basemodel

        Args:
            *args.
            **kwargs (dict): Key/value pairs
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary of __dict__ copy
        """
        bs_dict = (
            {
                k: (v.isoformat() if isinstance(v, datetime) else v)
                for (k, v) in self.__dict__.items()
            }
        )
        bs_dict["__class__"] = self.__class__.__name__
        return bs_dict

    def __str__(self) -> str:
        """print str representation of BaseModel."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
