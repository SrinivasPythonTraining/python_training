#!/usr/bin/python3

print("Hello world")

for num in range(10):
    print(num* 2)


class A:
    def __init__(self, a):
        self.a = a

    def display(self):
        print("Printing class variable", self.a)

x=A()
x.display()

