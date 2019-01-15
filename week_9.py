#Introduction to programming
#Sharing the expenses
#Prasun Biswas, 267948


# def main():
#     alphabetical_index = {}
#     while True:
#         line = input("Enter the topic and subconcept and the page number (end by an empty row):")
#         if line == "":
#             break
#
#         information = line.split()
#         topic = information[0]
#         subconcept=information[1]
#         page = int(information[2])
#
#         if topic not in alphabetical_index:
#             alphabetical_index[topic] = []
#         alphabetical_index[topic].append(page)
#
#     for topic in sorted(alphabetical_index):
#         print(topic, "", end="")
#         for nr in sorted(alphabetical_index[topic]):
#             print(nr, "", end="")
#         print()
#
#
# main()
def print_dict_order(input_dict):
   copy_dict = []
   copy_dict.clear()
   for key, value in input_dict.items():
       copy_dict.append((str(key)).strip()+ " " +(str(value)).strip())
       copy_dict.sort()
   print("Contestant score:")
   count=0
   for i in copy_dict:
       count+=1
       print(i)
       #print(i,'and count',count)

def print_list_in_dict(input_dict):
    person_cost = {}

    for person in sorted(input_dict):
        # print(person,"",end="")
        # print(sum(input_dict[person]))
        person_cost[person] = sum(input_dict[person])
    total_cost = sum(person_cost.values())
    avg_cost = total_cost / len(person_cost)
    print(f"Total costs: {round(total_cost,1)}0e")
    print()

    #print(f"cost per person {'{:.2f}'.format(round(avg_cost, 2))}e")

    for person in sorted(input_dict):
        #print(person,"",end="")
        personal_cost=person_cost.get(person)
        diff=avg_cost-personal_cost
        cost_str=""
        #print("diff is:",diff)
        print(f"{person} has paid {'{:.2f}'.format(round(personal_cost, 2))} in the following amounts: ",end="")
        #for nr in sorted(input_dict[person]):
        for nr in input_dict[person]:
            #print(f"{'{:.2f}'.format(round(nr, 2))}",end=" ")
            a_str=(f"{'{:.2f}'.format(round(nr, 2))}, ")
            cost_str=cost_str+a_str
            #print(a_str,end="")
        print(cost_str.rstrip(', '),end="")

        #print (input_dict[person],end="")
        print()
        if diff<0.05 and abs(diff)<0.05:
            print(f"  No transfers needed.")
        elif diff>0 and abs(diff)>=0.05:
            print(f"{person} needs to pay {'{:.2f}'.format(round(diff, 2))}e.")
        elif diff<0 and abs(diff)>=0.05:
            print(f"{person} needs to receive {'{:.2f}'.format(round(abs(diff), 2))}e.")

        print("")

# def add_list_in_dict(input_dict):
#     person_cost={}
#
#     for person in sorted(input_dict):
#         #print(person,"",end="")
#         #print(sum(input_dict[person]))
#         person_cost[person]=sum(input_dict[person])
#     total_cost=sum(person_cost.values())
#     avg_cost=total_cost/len(person_cost)
#     print(f"Total costs: {total_cost}e")
#     print(f"cost per person {avg_cost}e")
#   Moominmamma:3.3
#   Little My:1.3
#   Moominmamma:2.9
#   Snorkmaiden:2.2
#   Moominmamma:8.9
#   Moominpappa:3.9
#   Snorkmaiden:3.8
#   Moomintroll:2.2
#   Moominmamma:1.3
#   Snorkmaiden:2.0
#   Moomintroll:3.2
#   Moominmamma:5.0





def fix_filenames():
    input_dict={}
    file_name = input("Enter the name of the file: ")
    try:
        infile=open(file_name,'r')
        line=infile.readline()
        line_count=1
        while line:
            temp_list=line.split(":")
            person=temp_list[0]
            value1=temp_list[1]
            value=float(value1)
            #print('key', key,'value',value)
            if person not in input_dict:
                input_dict[person]=[]
            input_dict[person].append(value)

            #print(f"{line_count} {line}",end="")
            line = infile.readline()
            line_count+=1

        infile.close()
       # print_dict_order(input_dict)
        print_list_in_dict(input_dict)

        #add_list_in_dict(input_dict)

    #except FileNotFoundError as e:
        #print(e)
        #print("There was an error in reading the file.")
    except IndexError as e:
        #print(e)
        print("Error: there was an erroneous line in the file.")
        #print(line)
    except ValueError as e:
        #print(e)
        print("Error: there was an erroneous line in the file.")
        #print(value1)
    except:
        print(f"Error: file {file_name} cannot be read.")



fix_filenames()