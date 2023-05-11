#!/usr/bin/python3

import cmd
import json
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    classes = {1: "BaseModel", 2: "User"}
    notupdatable = {1: "id", 2: "created_at", 3: "updated_at"}

    def emptyline(self):
        """This is just ignoring an empty line"""
        pass
    
    def do_quit(self, line):
        """[quit] - This quit command exits the interface"""
        return True

    def do_EOF(self, line):
        """This allows us quit if a stream of commands is finished"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel aves it and prints the id"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if line == "" or args[0] not in self.classes.values():
            print("** class doesn't exist **")
            return
        
        if args[0] == "BaseModel":
            object0 = BaseModel()

        if args[0] == "User":
            object0 = User()

        print(object0.id)
        object0.my_number = 89
        object0.name = "My_Model"
        object0.save()

    def do_show(self, line):
        """Prints yhe string representation of an instances based on class name and id"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if line == "" or args[0] not in self.classes.values():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        f = open("file.json", "r")

        for line in f:
            for obj in json.loads(line).keys():
                objdata = obj.split(".")
                obj_id = objdata[1]
                print(objdata[0] == args[0])
                if obj_id == args[1]:
                    if objdata[0] == args[0]:
                        print(storage.all()[obj])
                        f.close()
                        return
        f.close()

        print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if line == "" or args[0] not in self.classes.values():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        f = open("file.json", "r")

        for line in f:
            for obj in json.loads(line).keys():
                objdata = obj.split(".")
                obj_id = objdata[1]
                if(obj_id == args[1]):
                    del storage.all()[obj]
                    storage.save()
                    return
        f.close()

        print("** no instance found **")

    def do_all(self, line):
        """Prints the string representation of all instances based or not based on class name"""
        all_objs = storage.all()

        if line == "":
            for obj in all_objs.values():
                print(obj)
            
            return

        if line not in self.classes.values():
            print("** class doesn't exist **")
            return

        args = line.split()

        if len(args) > 0:
            for obj in all_objs.keys():
                objdata = obj.split(".")
                if(objdata[0] == args[0]):
                    print(storage.all()[obj])
            
            return

    def do_convert(self, dt):
        return datetime.fromisoformat(str(dt))

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if line == "" or args[0] not in self.classes.values():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        f = open("file.json", "r")

        for line in f:
            for obj in json.loads(line).keys():
                objdata = obj.split(".")
                obj_id = objdata[1]
                if(obj_id == args[1]):
                    obj_decode = json.loads(line).values()

                    if args[2] not in obj_decode:
                        change = storage.all()[obj]
                        try:
                            value = float(args[3])
                            change.__dict__[args[2]] = value

                        except Exception:
                            word = str(args[3])
                            change.__dict__[args[2]] = word
                    
                        f.close()
                        storage.save()
                        return

                    if args[2] in self.notupdatable.values():
                        f.close()
                        return

                    val=type(storage.all()[obj].__dict__[args[2]])
                    change = storage.all()[obj]
                    change.__dict__[args[2]] = value(args[3])
                    f.close()
                    storage.save()
                    return
        f.close()

        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
