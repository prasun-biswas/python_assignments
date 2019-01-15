# TIE-02107: Programming 1: Introduction
# MAHABUB HASAN, mahabub.hasan@student.tut.fi, Student No.: 281749
# Solution of Task - 5.7.2

def main():

    # TODO: implement the datastructure for storing the board
    rows = 3
    cols = 3
    board = [['.', '.', '.'],
             ['.', '.', '.'],
             ['.', '.', '.']]
    for r in range (rows):
        for c in range (cols):
            print(board[r][c], end='')
        print()

    turns = 0  # How many turns have been played

    # The game continues until the board is full.
    # 9 marks have been placed on the board when the player has been
    # switched 8 times.
    while turns < 9:

        # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        coordinates = input("Player " + mark + ", give coordinates: ")

        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)
            if board[y][x] == '.':
                board[y][x]= mark
                for r in range(rows):
                    for c in range(cols):
                        print(board[r][c], end='')
                    print()
                if board[y][0]== board[y][1]== board[y][2] or board[0][x]== board[1][x]== board[2][x]:
                    print("The game ended, the winner is ", mark)
                    break
                elif board[0][0]==board[1][1]==board[2][2]== mark or board[0][2]==board[1][1]==board[2][0]== mark:
                    print("The game ended, the winner is ", mark)
                    break
                turns += 1
                if turns == 9:
                    print("Draw!")
            else:
                print("Error: a mark has already been placed on this square.")

        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")


main()
