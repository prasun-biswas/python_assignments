# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 4.5.1
# A program that calculates the angle of a triangle

def calculate_angle(first_angle, second_angle= 0):
    if second_angle==0:
        third_angle= 180 - 90 - first_angle
        return third_angle
    else:
        third_angle= 180 - (first_angle + second_angle)
        return third_angle


def main():
    #first_angle= int(input("Enter First angle: "))
    #second_angle = int(input("Enter Second angle: "))
    third_angle = calculate_angle(50,60)
    print("The third angle is ", third_angle)
    third_angle = calculate_angle(70)
    print("The third angle is ", third_angle)



main()
