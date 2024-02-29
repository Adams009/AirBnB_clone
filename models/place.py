#!/usr/bin/python3
"""Create a place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """create a place.

    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): name of place.
        description (str): place description.
        number_rooms (int): number of rooms.
        number_bathrooms (int): number of bathroom
        max_guest (int): maximum of guest.
        price_by_night (int): prices by the night.
        latitude (float): the latitude.
        longitude (float): the longitutde.
        amenity_ids (list): list of amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
