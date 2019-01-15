# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 3.6.3
# Parasetamol


def calculate_dose(weight, time, total_doze_24):
    amount_applicable = weight*15
    if time > 5:
        remain_dose = 4000-total_doze_24
        if remain_dose > amount_applicable:
            amount_can_given = amount_applicable
        else:
            amount_can_given = remain_dose
    else:
        amount_can_given = 0
    return amount_can_given



def main():

    weight=int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_doze_24= int(input("The total dose for the last 24 hours (mg): "))
    amount = calculate_dose(weight, time, total_doze_24)
    print("The amount of Parasetamol to give to the patient:", amount)


main()
