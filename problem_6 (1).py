#6.5: vowel and consonant

# def vowel_check(i):
#     if i=='a' or i=='e'or i=='i'or i=='o'or i=='u':
#         return True
#
# def main():
#     v_count=0
#     c_count=0
#
#     word=input("Enter a word: ")
#     for i in word:
#         if(vowel_check(i)):
#             v_count+=1
#         else:
#             c_count+=1
#     print(f"The word {word} contains {v_count} vowels and {c_count} consonants")
#
# main()

#6.6: ROT-13

# def encrypt(alphabet):
#     regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
#                      "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
#                      "w", "x", "y", "z"]
#     encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
#                        "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
#                        "j", "k", "l", "m"]
#     #
#     if alphabet in regular_chars:
#         index_reg_char=regular_chars.index(alphabet)
#         encr_char=encrypted_chars[index_reg_char]
#     elif alphabet.lower() in regular_chars:
#         index_reg_char=regular_chars.index(alphabet.lower())
#         encr_char=(encrypted_chars[index_reg_char]).upper()
#     else:
#         encr_char=alphabet
#     return encr_char
# def row_encryption(input_string):
#     empty_string=""
#     base_string=empty_string+input_string
#     encrypted_string=""
#     for i in base_string:
#         #print(f" encrypted in string operation: {encrypt(i)}")
#         encrypted_string=encrypted_string+encrypt(i)
#     return encrypted_string

# 6.7: saving a message
#
# def read_message():
#     list_of_string =[]
#     user_input =None
#     while user_input !="":
#         list_of_string.append(user_input)
#         user_input=input()
#     del list_of_string[0]
#     return list_of_string
# def main():
#     print("Enter text rows to the message. Quit by entering an empty row.")
#     msg = read_message()
#
#     print("The same, shouting:")
#     for i in msg:
#         print(i.upper())
# main()

# 6.8: ROT: whole message


def encrypt(alphabet):
    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    #
    if alphabet in regular_chars:
        index_reg_char=regular_chars.index(alphabet)
        encr_char=encrypted_chars[index_reg_char]
    elif alphabet.lower() in regular_chars:
        index_reg_char=regular_chars.index(alphabet.lower())
        encr_char=(encrypted_chars[index_reg_char]).upper()
    else:
        encr_char=alphabet

    return encr_char

def row_encryption(input_string):
    empty_string=""
    base_string=empty_string+input_string
    encrypted_string=""
    for i in base_string:
        #print(f" encrypted in string operation: {encrypt(i)}")
        encrypted_string=encrypted_string+encrypt(i)
    return encrypted_string


def read_message():
    list_of_strings = []
    user_input = None
    while user_input != "":
        list_of_strings.append(user_input)
        user_input = input()

    del list_of_strings[0]
    return list_of_strings


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for i in msg:
        print(row_encryption(i))

main()