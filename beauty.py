#!/usr/bin/python3

class Person():
    name = ""
    age = 12

    def __init__(self, name=None):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, ageNew):
        self.age = ageNew


Mark = Person("Mark")

Mark.setAge(30)

print(Mark.getAge(), Mark.name)

