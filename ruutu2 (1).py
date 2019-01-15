# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 3.6.2
# Template for task: ruutu

def read_input(order):
    value= int(input(order))
    while value <= 0:
        value = int(input(order))
    return value


def print_box(one, two, three):
    for x in range(1, two+1):
        print(three*one)

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print("")
    print_box(width, height, mark)


main()
