# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 3.6.1
# Area of Triangle

import math

def area(a, b, c):
    semiperimeter = a+b+c
    s = semiperimeter/2
    z = s*(s-a)*(s-b)*(s-c)
    result = math.sqrt(z)
    return result

def main():
    first_side = float(input("Enter the length of the first side: "))
    second_side = float(input("Enter the length of the second side: "))
    third_side = float(input("Enter the length of the third side: "))
    triangle_area = area(first_side, second_side, third_side)
    print("The triangle's area is", format(triangle_area, ".1f"))



main()



