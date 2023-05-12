#!/usr/bin/python3

import sys
import unittest


sys.path.append(".")
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_UUID(self):
        Mark = BaseModel()
        Andrew = BaseModel()
        self.assertNotEqual(Mark.id, Andrew.id)

    def test_Save(self):
        Mark = BaseModel()
        Mark.save()
        self.assertNotEqual(Mark.created_at, Mark.updated_at)

    def test_ToJSON(self):
        Micheal = BaseModel()
        Micheal.name = "Micheal"
        myjson = Micheal.to_dict()

        Michealnew = BaseModel(**myjson)

        self.assertEqual(Micheal.id, Michealnew.id)
    
    def test_SaveFileStorage(self):
        pass

    def test_ReloadFileStorage(self):
        pass

    def test_NewFileStorage(self):
        pass

    def test_AllFileStorage(self):
        pass


if __name__ == '__main__':
    from models.base_model import BaseModel
    unittest.main()
