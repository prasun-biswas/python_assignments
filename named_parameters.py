# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 4.5.2
# A program that prints box

def print_box(width, height, border_mark="#", inner_mark=" "):
    for x in range(1, height+1):
        for y in range(1, width+1):
            if x == 1 or x == height:
                print(border_mark, end="")
            elif y == 1 or y == width:
                print(border_mark, end="")
            else:
                print(inner_mark, end="")
        print()
    print()

def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(width=6, height=4, border_mark="O", inner_mark=".")

main()
