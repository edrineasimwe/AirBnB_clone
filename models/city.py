#!/usr/bin/python3
"""
    This modeule is for the City
    They are derived from the BaseModel
    and use the initialization function
    of the parent class

    __init__

    parameters:
        name
        state_id
"""

import models
from models.base_model import BaseModel


class City(BaseModel):
    """
        Derived from BaseModel class
        This class allows us store the Cities
        in a real world form

        Methods:

        Overriden Methods:
        __init__

        parameters:
            name
            state_id
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise a City Object
        using the BaseModel as a blue print
        """

        self.name = ""
        self.state_id = ""
        super().__init__(**kwargs)
