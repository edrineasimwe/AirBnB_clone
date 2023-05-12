#!/usr/bin/python3
"""
    This modeule is for the amenities
    They are derived from the BaseModel
    and use the initialization function
    of the parent class

    __init__

    parameters:
        name
"""

import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Derived from BaseModel class
        This class allows us store the amenities
        in a real world form

        Methods:

        Overriden Methods:
        __init__

        parameters:
            name
    """

    def __init__(self, *args, **kwargs):
        """
            Initialises the creation of an amenity
            Based on the real world object
        """
        self.name = ""
        super().__init__(**kwargs)
