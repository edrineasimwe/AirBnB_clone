#!/usr/bin/python3
import os
from io import StringIO
import unittest
from unittest.mock import Mock, patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def test_Numbers(self):
        self.assertEqual(1, 1)

    def test_ConsoleEmptyLine(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")

        self.assertEqual(f.getvalue(), "")

    def test_ConsoleAll(self):
        count = 0

        with patch('sys.stdout', new=StringIO()) as f:
            for i in range(3):
                HBNBCommand().onecmd("create User")

            HBNBCommand().onecmd("all")

            values = f.getvalue().split("\n")

            self.assertEqual(len(values[3:6]), 3)

            for i in range(3):
                HBNBCommand().onecmd(f'destroy User {values[i]}')

    def test_ConsoleAllC(self):
        count = 0

        with patch('sys.stdout', new=StringIO()) as f:
            for i in range(3):
                HBNBCommand().onecmd("create User")

            for i in range(2):
                HBNBCommand().onecmd("create Place")

            for i in range(1):
                HBNBCommand().onecmd("create City")

            HBNBCommand().onecmd("all")

            values = f.getvalue().split("\n")

            self.assertEqual(len(values[6:12]), 6)

            for i in range(6):
                HBNBCommand().onecmd(f'destroy User {values[i]}')
                HBNBCommand().onecmd(f'destroy Place {values[i]}')
                HBNBCommand().onecmd(f'destroy City {values[i]}')

    def test_ConsoleUpdate(self):
        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("create Place")

            id_0 = f.getvalue().split("\n")
            obj_id = id_0[0]

            HBNBCommand().onecmd(f'update')

            HBNBCommand().onecmd(f'update MyModel')

            HBNBCommand().onecmd(f'update Place')

            HBNBCommand().onecmd(f'update Place 1134 first_name Bob')

            HBNBCommand().onecmd(f'update Place {obj_id}')

            HBNBCommand().onecmd(f'update Place {obj_id} first_name')

            HBNBCommand().onecmd(f'update Place {obj_id} first_name Bob')

            HBNBCommand().onecmd("help update")

            intermediary = f.getvalue().split("\n")

            self.assertEqual("** class name missing **", intermediary[1])
            self.assertEqual("** class doesn't exist **", intermediary[2])
            self.assertEqual("** instance id missing **", intermediary[3])
            self.assertEqual("** no instance found **", intermediary[4])
            self.assertEqual("** attribute name missing **", intermediary[5])
            self.assertEqual("** value missing **", intermediary[6])

            token = "update [ClassName] [id] [attributeName] [attributevalue]"
            self.assertEqual(token, intermediary[7])
            self.assertEqual(token, intermediary[7])

            HBNBCommand().onecmd(f'destroy Place {obj_id}')

    def test_ConsoleCreate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create MyModel")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Review")
            HBNBCommand().onecmd("help create")

            values = f.getvalue().split("\n")

        self.assertEqual(values[0], "** class name missing **")
        self.assertNotEqual(values[1], "** class doesn't exist **")
        self.assertEqual(values[2], "** class doesn't exist **")
        self.assertNotEqual(values[3], "** class doesn't exist **")
        self.assertNotEqual(values[4], "** class doesn't exist **")
        self.assertNotEqual(values[5], "** class doesn't exist **")
        self.assertNotEqual(values[6], "** class doesn't exist **")
        self.assertNotEqual(values[7], "** class doesn't exist **")
        self.assertEqual(values[8], "Usage - create [classname] [ID]")

        HBNBCommand().onecmd(f'destroy User {values[1]}')
        HBNBCommand().onecmd(f'destroy Place {values[3]}')
        HBNBCommand().onecmd(f'destroy City {values[4]}')
        HBNBCommand().onecmd(f'destroy State {values[5]}')
        HBNBCommand().onecmd(f'destroy Amenity {values[6]}')
        HBNBCommand().onecmd(f'destroy Review {values[7]}')

    def test_ConsoleShow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

            id_0 = f.getvalue().split("\n")
            obj_id = id_0[0]

            HBNBCommand().onecmd(f'show')

            HBNBCommand().onecmd(f'show MyModel')

            HBNBCommand().onecmd(f'show Place')

            HBNBCommand().onecmd(f'show Place 1134')

            HBNBCommand().onecmd(f'show Place {obj_id}')

            HBNBCommand().onecmd("help show")

            intermediary = f.getvalue().split("\n")

            self.assertEqual("** class name missing **", intermediary[1])
            self.assertEqual("** class doesn't exist **", intermediary[2])
            self.assertEqual("** instance id missing **", intermediary[3])
            self.assertEqual("** no instance found **", intermediary[4])
            self.assertNotEqual("** no instance found **", intermediary[5])
            self.assertEqual("Usage - show [classname] [ID]", intermediary[6])

            HBNBCommand().onecmd(f'destroy Place {obj_id}')

    def test_ConsoleShow(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")

            id_0 = f.getvalue().split("\n")
            obj_id = id_0[0]

            HBNBCommand().onecmd(f'destroy')

            HBNBCommand().onecmd(f'destroy MyModel')

            HBNBCommand().onecmd(f'destroy Place')

            HBNBCommand().onecmd(f'destroy Place 1134')

            HBNBCommand().onecmd(f'destroy Place {obj_id}')

            HBNBCommand().onecmd("help destroy")

            inter = f.getvalue().split("\n")

            class_msg1 = "** class name missing **"
            class_msg2 = "** class doesn't exist **"
            inst1 = "** instance id missing **"
            inst2 = "** no instance found **"
            help0 = "Usage - destroy [classname] [ID]"

            self.assertEqual(class_msg1, inter[1])
            self.assertEqual(class_msg2, inter[2])
            self.assertEqual(inst1, inter[3])
            self.assertEqual(inst2, inter[4])
            self.assertEqual(help0, inter[5])
            self.assertEqual(help0, inter[5])
            os.remove('file.json')
