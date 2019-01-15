# TIE-02107: Programming 1: Introduction
# Solution of Task - 6.3
# A program that shows stats from recorded step counts

"""
group members:
    prasun biswas(267948)
    Mahbub hasan(281749)

"""

"""this returns the count number withing certain limits(low & high)
from a input list"""
def filter_by_steps(input_list, lower_lim, higher_lim):
    count_in_limit=0
    for i in input_list:
        if i>=lower_lim and i<=higher_lim:
            count_in_limit+=1
    return count_in_limit





""" this returns a list after removing the number which falls 
between certain lower and upper limit"""

def filter_list(input_list,lower_lim,higher_lim):
    filtered_list = []
    for i in input_list:
        if i not in range(lower_lim,higher_lim+1):
            # print(i)
            filtered_list.append(i)

    return filtered_list


""" it calculates the minimum number of catagories required to divide all of the
steps counts in a range of 4000 thousand starting from the minimum of 1000 steps
after passing a filtered list as an input which already excludes any measurements
below 1000"""


def divide_categories(filtered_list):
    max_step=max(filtered_list)+1
    lower_limits_of_category=[]
    number_of_category=(max_step-1000)//4000+((max_step-1000)%4000>0)
    # print(number_of_category)
    for i in range(1,number_of_category+1):
        nth_lower_limit=4000*i + (1000-4000)
        # print("nth lower",nth_lower_limit)
        lower_limits_of_category.append(nth_lower_limit)
    # print(lower_limits_of_category)
    return lower_limits_of_category


"""this generates graphical representation"""


def counts_in_category(lower_limit_list,alist):
    counts_in_category_list=[]
    digit = 5
    if len(str(max(lower_limit_list)))>5:
        digit = len(str(max(lower_limit_list)))
    # print("biggest digit", digit)
    print("Graphical representation of information:")
    for i in lower_limit_list:
        count=filter_by_steps(alist,i,i+3999)
        counts_in_category_list.append(count)
        print(f"{i:{digit}d} {count*'#'}")
        # print(f"count is {count} between {i} and {i+3999}")
    # print("counts in each category")
    # print(counts_in_category_list)
    max_counts_in_category=max(counts_in_category_list)
    index_max_count_category=counts_in_category_list.index(max_counts_in_category)


    lower_limit=lower_limit_list[index_max_count_category]
    print()
    print(f"Steps taken during most of the days: over {lower_limit} but under {lower_limit+4000} steps")






""" prints miscellaneous information about days over 9000 steps,
longest distance walked in a day and total calories burned"""


def miscellaneous(filtered_list):
    c_over_9000=filter_by_steps(filtered_list, 9000, (max(filtered_list) + 1))
    longest_dis_a_day=float(max(filtered_list))*1.5/2500
    total_steps_to_dis=float(sum(filtered_list))*1.5/2500
    total_calory=total_steps_to_dis*50
    if c_over_9000>=0:
        print(f"Days with over 9000 steps taken: {c_over_9000} days")

    if max(filtered_list)>=1000:
        print(f"Longest distance walked during a day: {format(longest_dis_a_day,'.2f')} km")

    print(f"Total calories consumed by walking: {int(round(total_calory))} kcal")




def main():

    print("Enter the amount of steps/day, one day per line.")
    print("End by entering an empty row.")

    list_of_steps =[]
    # user_input = None
    user_input = (input())
    while user_input !="":
        if user_input !='':
            int_user_input= int(user_input)
            list_of_steps.append(int_user_input)
            user_input = (input())
        else:
            break


    total_days=len(list_of_steps)
    rejected=filter_by_steps(list_of_steps, 0, 999)
    filtered_list=filter_list(list_of_steps,0,999)




    if total_days>0:
        print(f"Information related to the period of measurement ({total_days} days):")




    if rejected > 0:
        print(f"Rejected {rejected} results of under 1000 steps/day.")
    print()

    if len(filtered_list)>0:
        lower_limit_list=divide_categories(filtered_list)
        counts_in_category(lower_limit_list,filtered_list)


    # graphical_representation(filtered_list)
    if len(filtered_list)>0:
        miscellaneous(filtered_list)

    # print(list_of_steps)
    # print("steps in range",filter_by_steps(list_of_steps,5,10))

main()

