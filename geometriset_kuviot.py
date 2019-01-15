# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 4.4.4
# A program that calculates geometry shape


import math
def get_square():
    side = float(input("Enter the length of the square's side: "))
    while side == 0 or side < 0:
        side = float(input("Enter the length of the square's side: "))
        continue
    circumference = 4*side
    total_circumference = format(circumference, ".2f")
    print("The total circumference is ", str(total_circumference))
    area = side**2
    surface_area = format(area, ".2f")
    print("The surface area is", str(surface_area))

def get_rectangel():
    side_1 = float(input("Enter the length of the rectangle's side 1: "))
    while side_1 == 0 or side_1 < 0:
        side_1 = float(input("Enter the length of the rectangle's side 1: "))
        continue
    side_2 = float(input("Enter the length of the rectangle's side 2: "))
    while side_2 == 0 or side_2 < 0:
        side_2 = float(input("Enter the length of the rectangle's side 2: "))
        continue
    circumference = 2 * (side_1 + side_2)
    total_circumference = format(circumference, ".2f")
    print("The total circumference is", str(total_circumference))
    area = side_1 * side_2
    surface_area = format(area, ".2f")
    print("The surface area is", str(surface_area))

def get_circle():
    radius = float(input("Enter the circle's radius: "))
    while radius == 0 or radius < 0:
        radius = float(input("Enter the circle's radius: "))
        continue
    circumference = 2 * math.pi * radius
    total_circumference = format(circumference, ".2f")
    print("The total circumference is", str(total_circumference))
    area = math.pi * radius**2
    surface_area = format(area, ".2f")
    print("The surface area is", str(surface_area))


def menu():
    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if answer == "s":
            get_square()

        elif answer == "r":
            get_rectangel()

        elif answer == "c":
            get_circle()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


main()