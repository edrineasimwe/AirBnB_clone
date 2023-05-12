#!/usr/bin/python3
"""
    This module is for the State
    They are derived from the BaseModel
    and use the initialization function
    of the parent class

    __init__

    parameters:
        name
"""

import models
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class derives from the BaseModel Class

    It allows us store a State object efficiently
    Allowing us to put our efforts into manipulation

    parameters:
        name
    """

    def __init__(self, *args, **kwargs):
        """
        This initialises a state object allowing us
        manipulate it more efficiently
        """
        self.name = ""
        super().__init__(**kwargs)
