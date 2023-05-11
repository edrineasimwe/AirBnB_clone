#!/usr/bin/python3

import models
from models.base_model import BaseModel


class City(BaseModel):

    def __init__(self, *args, **kwargs):
        self.name = ""
        self.state_id = ""
        super().__init__(**kwargs)
