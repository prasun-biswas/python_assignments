# problem 2:

# user_ip = input("Answer Y or N: ")
#
# def check_user_ip(ip):
#     if ip.lower()=="y" or ip.lower()=="n":
#         print("You answered",ip)
#         return True
#     else:
#         return False
#
# while not check_user_ip(user_ip):
#     print("Incorrect entry.")
#     new_ip=input("Please retry: ")
#     if check_user_ip(new_ip):
#         break

#problem 3

# def main():
#     answer = input("Bored? (y/n) ")
#     while answer == "n" or answer == "N":
#         answer = input("Bored? (y/n) ")
#     while answer != "n" and answer != "y" and answer != "N" and answer != "Y":
#         print("Incorrect entry.")
#         answer = input("Please retry: ")
#         while answer == "n" or answer == "N":
#             answer = input("Bored? (y/n) ")
#     print("Well, let's stop this, then.")
#
# main()

#problem 2.3.1

# def main():
#     num = input("Choose a number: ")
#     for count in range (1,11,1):
#         multiplication = int(count)*int(num)
#         print(count, "*", num, "=", multiplication)
# main()

#problem 2.3.2

# def main():
#     num = input("Choose a number: ")
#     multiplication = 1
#     count = 1
#     while multiplication < 100:
#             multiplication = int(count) * int(num)
#             print(count, "*", num, "=", multiplication)
#             count = count + 1
# main()

#problem 2.3.3
# def main ():
#     num = int(input("How many numbers would you like to have? "))
#     for count in range(1, num+1, 1):
#         if (count)%3 == 0 and (count)%7 == 0:
#             print("zip boing")
#         elif (count)%7 == 0:
#             print("boing")
#         elif (count)%3 == 0:
#             print("zip")
#         else:
#             print(count)
#
# main()

#problem 2.5.1

# name = input("Tell us your name: ")
# print("Hey " + name + ", the printout formatting is going well!")

#problem 2.5.2
# def main():
#     PI = 3.14159265358979323846
#     print("The approximate value of pi is", format(PI,'.0f'), "or, if we want to get specific,", format(PI, '.4f'))
#
# main()

#problem 2.5.3
def main():
    for i in range(1, 11):
        for j in range(1, 11):
            multiplication = i*j
            print(format(multiplication, '4'), end="")
        print()

main()
