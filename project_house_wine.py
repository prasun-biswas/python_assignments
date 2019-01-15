
def out_temp_range(temp):

    if 20<=temp<=25:
        return True
    else:
        return False


def main():

    conseq_temp=0
    per_count=0
    num_of_measure=int(input("Enter the number of measurements: "))
    accept_percentage = num_of_measure/10


    if num_of_measure<=0:
        print("The number of measurements must be a positive number.")
    else:
        for x in range(num_of_measure):
            ip_string = f"Enter the temperature {x+1}: "
            cur_input=int(input(ip_string))

            if out_temp_range(cur_input):
                conseq_temp = 0
            else:
                conseq_temp+=1
                per_count+=1

                # print("conse temp",conseq_temp)
                if conseq_temp > 1 or per_count > accept_percentage:
                    print("Your wine is ruined.")
                    break
            if (x+1) == num_of_measure:
                print("Your wine is ready.")



main()