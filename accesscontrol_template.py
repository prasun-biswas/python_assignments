# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to programming
# Task: accesscontrol, program code template

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}


def valid_code(code):
    if code in DOORCODES:
        return True
    for d in DOORCODES:
        if code in DOORCODES[d]:
            return True
    return False


class Accesscard:

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.
        :param id: card holders personal id (str)
        :param name: card holders name (str)

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """

        self.id = id
        self.name = name

        self.codes = set()

    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """

        # TODO: Implement the method
        print(
            f'{self.id}, {self.name}, access: {", ".join(sorted(self.codes))}')

    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """

        # TODO: Implement the method
        return self.name

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.
        :param new_access_code: The accesscode to be added in the card.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # TODO: Implement the method
        self.codes.add(new_access_code)
        codes = list(self.codes)
        for c in codes:
            self.codes.remove(c)
            if c not in DOORCODES or not self.check_access(c):
                self.codes.add(c)

    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # TODO: Implement the methodc
        if door in self.codes:
            return True
        for d in DOORCODES:
            if d == door:
                for a in DOORCODES[d]:
                    if a in self.codes:
                        return True
        return False

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: The accesscard whose access rights are added to this card.
        :return:
        """

        # TODO: Implement the method
        for c in card.codes:
            self.add_access(c)


CARDS = {}


def main():
    # TODO: Implement the reading of the inputfile and storing the information.
    try:
        with open('accessinfo.txt', 'r') as f:
            for line in f:
                id, name, codes = line.strip().split(';')
                if not id or not name or ',' in id or ',' in name:
                    raise Exception()
                if id in CARDS:
                    raise Exception()

                card = Accesscard(id, name)
                for c in codes.split(','):
                    card.add_access(c)
                CARDS[id] = card
    except Exception as e:
        print('Error: file cannot be read.')
        return

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            # TODO: Excecute the command list here
            for c in sorted(CARDS):
                CARDS[c].info()

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]
            # TODO: Excecute the command info here
            if card_id not in CARDS:
                print('Error: unknown id.')
            else:
                card = CARDS[card_id].info()

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]
            # TODO: Excecute the command access here

            if card_id not in CARDS:
                print('Error: unknown id.')
            elif door_id not in DOORCODES:
                print('Error: unknown doorcode.')

            else:
                card = CARDS[card_id]
                if card.check_access(door_id):
                    print(
                        f'Card {card.id} ( {card.name} ) has access to door {door_id}')
                else:
                    print(
                        f'Card {card.id} ( {card.name} ) has no access to door {door_id}')

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]
            # TODO: Excecute the command add here
            if card_id not in CARDS:
                print('Error: unknown id.')
            elif not valid_code(access_code):
                print('Error: unknown accesscode.')
            else:
                card = CARDS[card_id]
                card.add_access(access_code)

        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]
            # TODO: Excecute the command merge here
            if card_id_to not in CARDS or card_id_from not in CARDS:
                print('Error: unknown id.')
            else:
                CARDS[card_id_to].merge(CARDS[card_id_from])
        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")


main()
