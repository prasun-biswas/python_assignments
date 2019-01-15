# TIE-02100 Johdatus ohjelmointiin

def find_unique_entry(input_list):
    output=[]
    seen=set()
    for value in input_list:
        if value not in seen:
            output.append(value)
            seen.add(value)
    # print("sorted output")
    # print(sorted(output))
    return sorted(output)


def count_occurance(uni_list,list_word_inputs):
    occur_dict={}
    for i in uni_list:
        count=list_word_inputs.count(i)
        occur_dict.setdefault(i,count)
    return occur_dict

def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    user_input=None
    build_string=""
    while user_input!="":
        user_input=input()
        build_string+=user_input+" "
    lc_build_string=build_string.lower()
    list_words=lc_build_string.split()
    #print(list_words)
    unique_list=find_unique_entry(list_words)
    occur_dict=count_occurance(unique_list,list_words)
    for key,value in occur_dict.items():
        print(key+" : "+str(value) + " times")


main()