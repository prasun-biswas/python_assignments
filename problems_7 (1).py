# TIE-02100 Johdatus ohjelmointiin

def print_dict_order(dict_en_sp):
    copy_dict = []
    for key in dict_en_sp.keys():
        copy_dict.append(key)
    # sorted(copy_dict)
    copy_dict.sort()
    string_values = ", ".join(copy_dict)
    return string_values


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print("Dictionary contents:")
    print(print_dict_order(english_spanish))

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            user_input = input("Enter the word to be translated: ")
            return_value = english_spanish.get(user_input, user_input)
            if user_input in english_spanish.keys():
                print(user_input, "in Spanish is", return_value)
            else:
                print("The word", user_input, "could not be found from the dictionary.")

        elif command == "A":
            input_key = input("Give the word to be added in English: ")
            input_value = input("Give the word to be added in Spanish: ")
            if input_key in english_spanish.keys():
                temp_dict = {input_key: input_value}
                english_spanish.update(temp_dict)
            else:
                english_spanish.setdefault(input_key, input_value)
            print("Dictionary contents:")
            print(print_dict_order(english_spanish))

        elif command == "R":
            input_remove = input("Give the word to be removed: ")
            if input_remove in english_spanish.keys():
                del english_spanish[input_remove]
            else:
                print("The word", input_remove, "could not be found from the dictionary.")
            # print("Dictionary contents:")
            # print(print_dict_order(english_spanish))


        elif command == "Q":
            print("Adios!")
            return

        elif command == "P":
            copy_dict = []
            for key, value in english_spanish.items():
                copy_dict.append(key + " " + value)
            # sorted(copy_dict)
            copy_dict.sort()
            for i in copy_dict:
                print(i)
        elif command == "T":
            empty_string = ""
            sentense = input("Enter the text to be translated into Spanish: ")
            list_values = sentense.split(" ")
            for i in list_values:
                empty_string += " " + english_spanish.get(i, i)
            print("The text, translated by the dictionary:")
            print(empty_string.lstrip())

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


main()