# 1.2.5
# print("Hello World!")

# 1.3.1
# name = input("Tell your name: ")
# print("Hi " + name + ", your coding skills are great!")

# 1.3.2
# benefit=float(input("Enter the amount of the study benefits: "))
# print("If the index raise is 1.17 percent, the study benefit,")
# percent=float(1.17/100)
# new_benefit=float(benefit+benefit*percent)
# print("after a raise, would be "+str(new_benefit)+" euros")
# extra_bonus=str(new_benefit+new_benefit*percent)
# print("and if there was another index raise, the study")
# print("benefits would be as much as "+extra_bonus+" euros")

emoji=[":'(",":-(",":-|",":-)",":-D",]

ask_feelings=int(input("How do you feel? (1-10) "))
if ask_feelings ==1:
    print("A suitable smiley would be "+emoji[0])
elif ask_feelings==10:
    print("A suitable smiley would be "+emoji[4])
elif ask_feelings >1 and ask_feelings<4:
    print("A suitable smiley would be "+emoji[1])
elif ask_feelings>=4 and ask_feelings<=7:
    print("A suitable smiley would be "+emoji[2])
elif ask_feelings >7 and ask_feelings<10:
    print("A suitable smiley would be "+emoji[3])
else:
    print("Bad input!")



