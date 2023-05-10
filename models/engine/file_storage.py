#!/usr/bin/python3

from datetime import datetime
import json
from ..base_model import BaseModel


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        newentry = f'{str(type(obj).__name__)}.{obj.id}'
        self.__objects[newentry] = obj

    def save(self):
        f = open(self.__file_path, "w")
        for obj in self.__objects.keys():
            model = {obj: self.__objects[obj].to_dict()}
            jobj = json.dumps(model)
            f.write(jobj)
            f.write("\n")
        model.clear()
        f.close()

    def reload(self):
        try:
            f = open(self.__file_path)
            for line in f:
                object0 = json.loads(line)
                for object1 in object0.values():
                    reloadi = BaseModel(**object1)
                    datetime.fromisoformat(str(reloadi.updated_at))
                    datetime.fromisoformat(str(reloadi.created_at))
                    newentry = f'{str(type(reloadi).__name__)}.{reloadi.id}'
                    self.__objects[newentry] = reloadi
                object0.clear()
            f.close()

        except Exception:
            pass
