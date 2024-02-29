#!/usr/bin/python3
"""The Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """create a review.

    Attributes:
        place_id (str): place id
        user_id (str): User id.
        text (str): text of review.
    """

    place_id = ""
    user_id = ""
    text = ""
