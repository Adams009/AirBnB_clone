#!/usr/bin/python3
"""The city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Create a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of city.
    """

    state_id = ""
    name = ""
