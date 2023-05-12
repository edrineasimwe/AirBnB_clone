#!/usr/bin/python3
"""
    This modeule is for the Place
    They are derived from the BaseModel
    and use the initialization function
    of the parent class

    __init__

    parameters:
        name
        city_id
        user_id
        description
        number_rooms
        amenity_ids
        longitude
        latitude
        price_by_night
        max_guest
        number_bathrooms
"""

import models
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Derived from BaseModel class
        This class allows us store the Places
        in a real world form

        Methods:

        Overriden Methods:
        __init__

        parameters:
            name
            user_id
            city_id
            description
            number_rooms
            amenity_ids
            longitude
            latitude
            price_by_night
            max_guest
            number_bathrooms
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises a Place with given arguments using
        it's parents initialisation method
        """

        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

        super().__init__(**kwargs)
