#!/usr/bin/python3
"""
    This module is for the Revies
    They are derived from the BaseModel
    and use the initialization function
    of the parent class

    __init__

    parameters:
        name
        user_id
        text
"""

import models
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Derived from BaseModel class
        This class allows us store the Reviews
        in a real world form

        Methods:

        Overriden Methods:
        __init__

        parameters:
            name
            text
            user_id
    """

    def __init__(self, *args, **kwargs):
        """Allows us create a Review
        from the given arguments
        """

        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(**kwargs)
