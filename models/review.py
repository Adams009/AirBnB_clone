#!/usr/bin/python3
"""Module base_model

The Module Review Class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class of review

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): The text
    """

    place_id = ""
    user_id = ""
    text = ""
