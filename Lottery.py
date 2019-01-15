# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 4.4.3
# A program that calculates probability to guess a ball correctly


# Probability function to guess the ball correctly
def get_probability(lottery_ball, drawn_ball):
    ball = 1
    drawn = 1
    result = lottery_ball - drawn_ball
    difference = 1

    if drawn_ball < 0 or lottery_ball < 0:
        print("The number of balls must be a positive number.")
    elif drawn_ball > lottery_ball:
        print("At most the total number of balls can be drawn.")

    else:

        for x in range(1, lottery_ball + 1, 1):
            ball = x * ball

        for y in range(1, drawn_ball + 1, 1):
            drawn = y * drawn

        for z in range(1, result + 1, 1):
            difference = difference * z

        drawn_way = ball // (drawn * difference)

        print("The probability of guessing all", str(drawn_ball),
              "balls correctly is 1/" +str(drawn_way))


def main():
    lottery_ball = int(input("Enter the total number of lottery balls: "))
    drawn_ball = int(input("Enter the number of the drawn balls: "))
    get_probability(lottery_ball, drawn_ball)


main()



