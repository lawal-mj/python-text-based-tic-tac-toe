import sys
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


# display_board()


def end_game():
    print("The game has ended")
    sys.exit()

def player_one_play(player_one_tag):
    number = int(input(player_one_tag + " pick a number on the board: "))
    board[number] = player_one_tag
    display_board()

def player_two_play(player_two_tag):
    number = int(input(player_two_tag + " pick a number on the board: "))
    board[number] = player_two_tag
    display_board()




def start_game():
    print("The game has started, players pick a tag")
    player_one = input("Player 1: ")
    player_two = input("Player 2: ")
    print("Player 1 and 2 are " + player_one + " and " + player_two + " respectively")
    print("This is the game board, pick a number starting from player one to play")
    display_board()
    player_one_play(player_one)
    player_two_play(player_two)



start_game()

# takes in player one and two tags 



def check_winner():
    print("Chechking....")