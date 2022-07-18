"""
Factory Coding Exercise:
- You are given a class called Person. The person has 2 attrs: id, name.
- Please implement a PersonFactory that has a non-static create_person()
method that takes a person's name and return a person initialized with this
name and an id.
- The id of the person should be set as a 0-based index of the object created.
So, the first person the factory makes should have Id=0, so on
"""


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    idx = 0

    def create_person(self, name):
        p = Person(id=self.idx, name=name)
        self.idx += 1
        return p
