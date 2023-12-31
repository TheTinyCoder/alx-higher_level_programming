#!/usr/bin/python3
import sys
sys.path.append('../')
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle = Rectangle(10)
print("{} - {} => {} / {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area(), my_rectangle.perimeter()))
