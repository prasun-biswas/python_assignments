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


def main():
    input_dict={}
    file_name = input("Enter the name of the score file: ")
    try:
        infile=open(file_name,'r')
        line=infile.readline()
        line_count=1
        while line:
            temp_list=line.split(" ")
            key=temp_list[0]
            value1=temp_list[1]
            value=int(value1)
            #print('key', key,'value',value)
            if key in input_dict:
                    #print(temp_list[0],'key and value',temp_list[1])
                    pre_value=int(input_dict.get(key))
                    current_value=pre_value+int(value)
                    #print("pre value",pre_value, "current value",current_value)
                    input_dict[key]=current_value
            else:
                    input_dict[key]=value
                    #print('value added')

            #print(f"{line_count} {line}",end="")
            line = infile.readline()
            line_count+=1

        infile.close()
        print_dict_order(input_dict)
    #except FileNotFoundError as e:
        #print(e)
        #print("There was an error in reading the file.")
    except IndexError as e:
        #print(e)
        print("There was an erroneous line in the file:")
        print(line)
    except ValueError as e:
        #print(e)
        print("There was an erroneous score in the file:")
        print(value1)
    except:
        print("There was an error in reading the file.")



main()
