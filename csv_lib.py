import csv


def main():
    file = input('Enter the name of the input file: ')
    in_dialect = input('and its dialect: ')
    out_file = input('Enter the name of the output file: ')
    out_dialect = input('and its dialect: ')

    all_dialects = csv.list_dialects()


    if in_dialect not in all_dialects or out_dialect not in all_dialects:
        print('\nThe given dialect is wrong.')
        return

    try:
        f = open(file, newline='')
        reader = csv.reader(f, dialect=in_dialect)
    except IOError:
        print('\nThere was an error in handling the file.')
        return

    with open(out_file, 'w', newline='') as f:
        try:
            writer = csv.writer(f, dialect=out_dialect)
            for row in reader:
                writer.writerow(row)
        except IOError:
            print('\nThere was an error in handling the file.')
            return

    print(f'\nFile {file} has been converted into {out_dialect}.')


main()
