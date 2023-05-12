#!/usr/bin/python3

import cmd
import json
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        This is a class meant to cater for the interactive
        side of the airBnB clone application. 
        It only accepts a few classes and creates them ie

        Classes:
            BaseModel
            User
            Place
            City
            Review
            Amenity
            State

        Methods or commands include:
        show
        all
        update
        destroy
        create

        Although the user can decide to use more
        specific commands like
        User.all()
        Place.destroy('id')
        City.count()
        Amenity.update('id', attribute_name attribute_value)
        User.update('id', {'attribute_name : attribute_value'})
        USer.show('id')
    """

    prompt = '(hbnb)'

    classes = {1: "BaseModel",
               2: "User",
               3: "Place",
               4: "State",
               5: "City",
               6: "Amenity",
               7: "Review"}
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
        """Usage - create [classname] [ID]"""
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

        if args[0] == "Place":
            object0 = Place()

        if args[0] == "State":
            object0 = State()

        if args[0] == "City":
            object0 = City()

        if args[0] == "Amenity":
            object0 = Amenity()

        if args[0] == "Review":
            object0 = Review()

        print(object0.id)
        object0.my_number = 89
        object0.name = "My_Model"
        object0.save()

    def do_show(self, line):
        """Usage - show [classname] [ID]"""
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

                if obj_id == args[1]:
                    if objdata[0] == args[0]:
                        print(storage.all()[obj])
                        f.close()
                        return
        f.close()

        print("** no instance found **")

    def do_destroy(self, line):
        """Usage - destroy [classname] [ID]"""
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
                if obj_id == args[1]:
                    if args[0] == objdata[0]:
                        del storage.all()[obj]
                        storage.save()
                        f.close()
                        return
        f.close()

        print("** no instance found **")

    def do_all(self, line):
        """Prints the string representation of all instances
        based or not based on class name"""
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

    def do_update(self, line):
        """update [ClassName] [id] [attributeName] [attributevalue]"""
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

                    if objdata[0] == args[0]:
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

                    f.close()
                    storage.save()
                    return
        f.close()

        print("** no instance found **")

    def count(self, line):
        """
            A simple function that handles
            the counting part of the 
            <class_name>.count()
            additional feature
        """
        count = 0
        all_objs = storage.all()

        if line not in self.classes.values():
            print("** class doesn't exist **")
            return

        args = line.split()

        if len(args) > 0:
            for obj in all_objs.keys():
                objdata = obj.split(".")
                if(objdata[0] == args[0]):
                    count = count + 1
        print(count)

    def default(self, line):
        """
            This was created as part of the
            advanced assignment

            It handles the special commands such as
            User.count()
            Place.all()
            and so many others
        """
        args = line.split(".")
        second_parsing = args[1].split("(")

        line_parsed = f'{args[0]}'

        if second_parsing[0] == "all":
            self.do_all(line_parsed)

        if second_parsing[0] == "count":
            self.count(line_parsed)

        if second_parsing[0] == "show":
            intermediat1 = args[1].split('"')

            line_parsed_ext = line_parsed + " " + intermediat1[1]
            self.do_show(line_parsed_ext)

        if second_parsing[0] == "destroy":
            intermediat1 = args[1].split('"')

            line_parsed_ext = line_parsed + " " + intermediat1[1]
            self.do_destroy(line_parsed_ext)

        if second_parsing[0] == "update":
            start = line.split(", {")

            if len(start) == 1:
                intermediat1 = args[1].split('"')
                line_parsed1 = line_parsed + " " + intermediat1[1]
                line_parsed1 += " " + intermediat1[3]
                line_parsed1 += " " + intermediat1[5]

                self.do_update(line_parsed1)

            else:
                start[1] = start[1][:-2]
                fields = start[1].split(", ")
                for field in fields:
                    intermid = field.split(": ")
                    first = intermid[1][0]
                    if first == "'" or first == '"':
                        first = intermid[1][1:-1]

                    else:
                        first = intermid[1]

                    intermediat1 = args[1].split('"')
                    line_parsed1 = line_parsed + " " + intermediat1[1]
                    line_parsed1 += " " + intermid[0][1:-1]
                    line_parsed1 += " " + first

                self.do_update(line_parsed1)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
