# 1. have a board be displayed everytime

# 2. allow the player pick a spot based on index location


board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# print(board)

def display_board():
    print(" ", board[1], "|", board[2], "|", board[3])
    print(" ----------- ")
    print(" ", board[4], "|", board[5], "|", board[6])
    print(" ----------- ")
    print(" ", board[7], "|", board[8], "|", board[9])


display_board()