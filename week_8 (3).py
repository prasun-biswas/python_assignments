import os

def if_mp3(input):
    compare_str="mp3"
    input_string=""+input
    temp_list=input_string.split(".")
    if temp_list[1]!=compare_str:
        return input
    else:
        name=input_string.rstrip('.mp3')
        return check_name_valid(name)

def check_name_valid(name):
    #print(name)
    temp_list=name.split("-")
    if len(temp_list)==3:
        song=temp_list[2]
        artist=temp_list[1]
        correct_name=f"{song}-{artist}.mp3"
        #print(f"corrected name:{correct_name}")
        return correct_name
    else:
        correct_name=f"{name}.mp3"
        #print(f"corrected name:{correct_name}")
        return correct_name




def fix_filenames(path):
    os.chdir(path)
    for items in os.listdir():
        if not items.endswith('.mp3'):
            continue

        file_name_divs = items.split('-')
        if not file_name_divs[0].isdigit():
            continue

        try:
            os.rename(items, file_name_divs[2][:-4] + '-' + file_name_divs[1] + '.mp3')
        except Exception as error:
            pass

#fix_filenames()

