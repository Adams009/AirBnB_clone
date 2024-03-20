#!/usr/bin/python3
"""Module base_model

The Module for Place Class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """class of a place

    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): name of place.
        description (str): description of place.
        number_rooms (int): number of rooms available
        number_bathrooms (int): number of bathrooms available
        max_guest (int): maximum number of guests
        price_by_night (int): price by night
        latitude (float): latitude of place.
        longitude (float): longitude of place.
        amenity_ids (list): Amenity ids.
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
