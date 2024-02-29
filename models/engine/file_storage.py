#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ The FileStorage class for serialization and deserialization

    Attributes:
        __file_path (str): The path to the JSON file
        __objects (dict): A dictionary to store instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return dictionary

        Returns:
            dict: The dictionary of all instances.
        """
        return self.__objects

    def new(self, obj):
        """ Adds a new instance

        Parameters:
        - obj: An instance to be added
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes the dictionary to a JSON file. """

        serial_objects = []
        for key, obj in self.__objects.items():
            serial_object = {key: obj.to_dict()}
            serial_objects.append(serial_object)

        with open(self.__file_path, 'w') as new_file:
            json.dump(serial_objects, new_file)
