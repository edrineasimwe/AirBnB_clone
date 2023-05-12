#!/usr/bin/python3

"""
    This module deals with setting up a basic structure that
    is used to give life to all other subclasses
    such as Amenities, City, Places and others

    It includes the following methods:
    save()
    to_dict()
    __init__()
    __str__()
    convert_to_accepted_format()
"""

import models
from datetime import datetime
import uuid


class BaseModel(object):
    """
        This is the base model class that
        parents all real word objects
        of this application

        Methods:
        save() - saves object to file storage
        to_dict() - converts an object to its dictionary form
                    and preps it for serialization

        convert_to_accepted_format() - turns datettime objects
                                    to strings for easy
                                    serialization

        Overriden methods include:
        __init__
        __str__
    """

    def __init__(self, *args, **kwargs):
        """
            Initialises an object that is the
            foundation of all that makes the
            application even function

            #incase no argument is
            provided a basic object is instantiated
            otherwise an  object is instantiated with
            values in the argument

            It only allows dictionaries
            Other data structures wont work just as
            well
        """
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

        models.storage.new(self)

    def __str__(self):
        """
            Produces a representation of an object in the form
            ClassName.Class_id : class_dictionary_repressentation
        """
        firstly = f'[{type(self).__name__}] ({self.id})'
        secondly = f'{firstly} {self.__dict__}'
        return secondly

    def save(self):
        """
            Updates the updated_at variable to current time
            Then saves the object instance to the file storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def convert_to_accepted_format(self):
        """
            Converts the datetime variables to their string
            representation to make it easier to store for the
            file storage engine
        """
        t1 = datetime.fromisoformat(str(self.updated_at))
        t2 = datetime.fromisoformat(str(self.created_at))

        self.__dict__["updated_at"] = t1
        self.__dict__["created_at"] = t2

    def to_dict(self):
        """
            Parses a object returning it's dictionary
            representation that can be serialised
            into json form
        """
        self.convert_to_accepted_format()
        self.__dict__["__class__"] = str(type(self).__name__)
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__["created_at"] = self.created_at.isoformat()
        return self.__dict__
