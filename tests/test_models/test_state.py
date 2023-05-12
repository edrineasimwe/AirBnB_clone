#!/usr/bin/python3
"""
This module is to test the correct working of the
State class.

It includes:
    Testing distinct uuids
    Testing save functionality
    Testing it's conversion to json
    Testing it's conversion to a dictionary
    Testing that it can be saved to a file
"""

import sys
import os
import unittest
import json
import models
from models import storage
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
        This class is the one that handles
        all the testing of the State class

        It's methods include:
            test_UUID()
            test_Save()
            test_ToJSON()
            test_toDict()
            test_SaveStorage()
    """

    def test_UUID(self):
        """
        Tests to see whether two instances can have the same id
        """
        Mark = State()
        Andrew = State()
        self.assertNotEqual(Mark.id, Andrew.id)

    def test_Save(self):
        """
        Tests to see if an instance can be updated
        """
        Mark = State()
        Mark.save()
        self.assertNotEqual(Mark.created_at, Mark.updated_at)

    def test_ToJSON(self):
        """
        Tests to see if an instance can be converted
        to and from json form
        """
        Micheal = State()
        Micheal.name = "Micheal"
        old_json = json.dumps(Micheal.to_dict())
        new_json = json.loads(old_json)

        Michealnew = State(**new_json)

        self.assertEqual(Micheal.id, Michealnew.id)

    def test_toDict(self):
        """
        Tests to see if an instance can be converted to
        it's dictionary form
        """
        Mick = State()

        Mick.to_dict()

        self.assertEqual(Mick.__dict__["__class__"], "State")

    def test_SaveStorage(self):
        """
        Tests to see if an instance can be saved
        and retrieved
        """
        Micheal = State()
        Micheal.save()

        myobjs = storage.all()
        for obj in myobjs.values():
            if obj.id == Micheal.id:
                self.assertEqual(obj.id, Micheal.id)

        os.remove('file.json')


if __name__ == '__main__':
    from models.state import State
    unittest.main()
