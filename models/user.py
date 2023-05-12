#!/usr/bin/python3
"""
    This modeule is for the User
    They are derived from the BaseModel
    and use the initialization function
    of the parent class

    __init__

    parameters:
        email
        password
        first_name
        last_name
"""

from models.base_model import BaseModel
import models


class User(BaseModel):
    """
        Derived from BaseModel class
        This class allows us store the User
        in a real world form

        Methods:

        Overriden Methods:
        __init__

        parameters:
            first_name
            password
            email
            last_name
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises a review based on
        the provided arguments
        """

        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(**kwargs)
