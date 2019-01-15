# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 4.4.2
# A program that compares two float numbers


def compare_floats(number1, number2, EPSILON):
    if abs(number1 - number2) < EPSILON:
        return True
    else:
        return False
def main():
    EPSILON = 0.000000001
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    result = compare_floats(number1, number2, EPSILON)
main()
