#!/usr/bin/python3
"""Module base_model

The Module User Class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class for user.

    Attributes:
        email (str): The emai
        password (str): The password
        first_name (str): The first name
        last_name (str): The last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
