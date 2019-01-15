def print_in_accordance_of_values(english_spanish):
    for b in sorted(english_spanish, key=lambda a : english_spanish[a]):
        print(english_spanish[b], b)

def main():
    english_spanish = {"hi": "hola", "thanks": "gracias", "yes": "si", "no": "no"}
    result = print_in_accordance_of_values(english_spanish)
main()