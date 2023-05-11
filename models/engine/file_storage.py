#!/usr/bin/python3

from datetime import datetime
import json
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


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

        if len(self.__objects) == 0:
            f.write("")
            f.close()
            return

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
                    if object1["__class__"] == "BaseModel":
                        reloadi = BaseModel(**object1)

                    if object1["__class__"] == "User":
                        reloadi = User(**object1)

                    if object1["__class__"] == "City":
                        reloadi = City(**object1)

                    if object1["__class__"] == "Amenity":
                        reloadi = Amenity(**object1)

                    if object1["__class__"] == "Place":
                        reloadi = Place(**object1)

                    if object1["__class__"] == "Review":
                        reloadi = Review(**object1)

                    if object1["__class__"] == "State":
                        reloadi = State(**object1)

                    datetime.fromisoformat(str(reloadi.updated_at))
                    datetime.fromisoformat(str(reloadi.created_at))
                    newentry = f'{str(type(reloadi).__name__)}.{reloadi.id}'
                    self.__objects[newentry] = reloadi
                object0.clear()
            f.close()

        except Exception:
            pass
