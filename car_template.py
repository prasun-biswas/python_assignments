# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 4.6
# Car simulation


import math


def menu():
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


# This function has three parameters which are all FLOATs:
#       (1) the size of the tank
#       (2) the amount of gas that is requested to be filled in
#       (3) the amount of gas in the tank currently
#
# The parameters have to be in this order.
# The function returns one FLOAT that is the amount of gas in the
# tank AFTER the filling up.
#
# The function does not print anything and does not ask for any
# input.

def fill(tank_size, to_fill, remain):
    if to_fill < tank_size - remain:
        remain = to_fill + remain
    else:
        remain = (tank_size - remain) + remain

    return remain



# This function has six parameters. They are all floats.
#   (1) The current x coordinate
#   (2) The current y coordinate
#   (3) The destination x coordinate
#   (4) The destination y coordinate
#   (5) The amount of gas in the tank currently
#   (6) The consumption of gas per 100 km of the car
#
# The parameters have to be in this order.
# The function returns three floats:
#   (1) The amount of gas in the tank AFTER the driving
#   (2) The reached (new) x coordinate
#   (3) The reached (new) y coordinate
#
# The return values have to be in this order.
# The function does not print anything and does not ask for any
# input.


def drive(x, y, new_x, new_y, gas, gas_consumption):
    if x == 0 and y==0 and new_x == 0 and new_y == 0:
        x=0
        y=0
        remain = gas
        return remain, x, y
    else:
        distance_to_go = math.sqrt((new_x - x) ** 2 + (new_y - y) ** 2)
        distance_per_lr = 100 / gas_consumption
        gas_required = distance_to_go / distance_per_lr
        if gas_required <= gas:
            distance_gone = distance_to_go
        else:
            distance_gone = gas * distance_per_lr

        x, y = coordinates(x, y, new_x, new_y, distance_gone, distance_to_go)

        remain = remain_gas(gas, distance_gone, distance_per_lr)

        return remain, x, y


def coordinates(x, y, new_x, new_y, distance_gone, distance_to_go):
    x= x + (((new_x-x)*distance_gone)/distance_to_go)
    y = y + (((new_y - y) * distance_gone) / distance_to_go)
    return x,y


def remain_gas(gas, distance_gone, distance_per_lr ):
    remain = gas - (distance_gone / distance_per_lr)
    return remain

# Implement your own functions here. It is required to implement at least
# two functions that take at least one parameter and return at least one
# value.
# The functions have to be used somewhere in the program.


def read_number(prompt, error_message="Incorrect input!"):

    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()

main()
