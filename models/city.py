#!/usr/bin/python3
"""Module base_model

This Module contains City Class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """A class that city

    Attributes:
        name (str): name of city
        state_id (str): state id
    """

    state_id = ""
    name = ""
