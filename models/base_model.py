#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel():

    def __init__(self, *args, **kwargs):

        if kwargs:
            self.__dict__ = kwargs
            t1 = datetime.fromisoformat(kwargs["updated_at"])
            t2 = datetime.fromisoformat(kwargs["created_at"])

            self.__dict__["updated_at"] = t1
            self.__dict__["created_at"] = t2
            del self.__dict__["__class__"]
            return

        self.id = str(uuid.uuid4())
        date_time = datetime.now()
        self.created_at = date_time
        self.updated_at = date_time

    def __str__(self):
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__["__class__"] = str(type(self).__name__)
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__["created_at"] = self.created_at.isoformat()
        return self.__dict__
