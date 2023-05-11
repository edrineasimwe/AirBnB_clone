#!/usr/bin/python3

from models.base_model import BaseModel
import models


class User(BaseModel):
    
    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__()
