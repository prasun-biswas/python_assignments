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

def main():
    num = input("Choose a number: ")
    for count in range (1,11,1):
        multiplication = int(count)*int(num)
        print(count, "*", num, "=", multiplication)
main()
    