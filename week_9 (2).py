# TIE-02100 Johdatus ohjelmointiin
# Read genres and tv-series from a file into a dict.
# Print a list of the genres in alphabetical order
# and list tv-series by given genre on user's command.


def read_file(filename):
    # reads and saves the series and their genres from the file
    my_set=set()
    #print("genre list:",my_set)
    store={}
    # TODO initialize a new data structure

    try:
        file = open(filename, "r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")
            my_set.update(genres)

            if name not in store:
                store[name]=genres




            # TODO add the info to the data structure
        file.close()
        sorted(my_set)
        print("Available genres are: ",end="")
        #print(my_set)
        y = ", ".join(str(i) for i in sorted(my_set))
        print(y)


        return  store
        # TODO return the data structure

    except ValueError as e:
        print("Error: rows were not in the format name;genres.")
        print(e)
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():

    filename = input("Enter the name of the file: ")
    TODO = read_file(filename)

    # TODO print the genres

    while True:
        genre = input("> ")

        if genre == "exit":
            return
        found_list=[]
        for key,value in TODO.items():
            #print(key)
            #print(value)
            if genre in value:
                found_list.append(key)
        for i in sorted(found_list):
            print(i)

        # TODO print the series ...

main()