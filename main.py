#!/usr/bin/python3

print("Hello world")


class A:
    def __init__(self, a):
        self.a = a

    def display(self):
        print("Printing class variable", self.a)

x=A(10)
x.display()

for num2 in range(20):
    print(num2)
