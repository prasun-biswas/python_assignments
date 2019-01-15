# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 5.4.4


def main():
    performance1 = float(input('Enter the time for performance 1: '))
    performance2 = float(input('Enter the time for performance 2: '))
    performance3 = float(input('Enter the time for performance 3: '))
    performance4 = float(input('Enter the time for performance 4: '))
    performance5 = float(input('Enter the time for performance 5: '))
    performance = [performance1, performance2, performance3, performance4, performance5]
    best = min(performance)
    worst = max(performance)
    remove = best+worst
    total = get_total(performance)
    total = total - remove
    average = total/(len(performance)-2)
    print("The official competition score is", format(average, ".2f"), "seconds.")

def get_total(performance):
    total = 0
    for number in performance:
        total = total + number
    return total

main()