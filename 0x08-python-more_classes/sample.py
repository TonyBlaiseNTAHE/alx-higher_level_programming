#!/usr/bin/python3

class Men:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name}"


if __name__ == '__main__':
    my_guy = Men("Tony")
    print(my_guy)
    print(type(my_guy))