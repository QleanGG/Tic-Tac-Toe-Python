import os
from enum import Enum
import random

class Actions(Enum):
    Player = 1
    CPU = 2
    Exit = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# winning combinations for tic tac toe
winningCombinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
]

def menu():
    print ("Welcome to Tic Tac Toe! \n")
    print ("Press 1 to play against another player")
    print ("Press 2 to play against the computer")
    print ("Press 0 to exit")

# changes turn for player game
def user_turn(choice,game_arr,letter):
    game_arr[choice-1] = letter
    if letter == 'X': return 'O'
    if letter == 'O': return 'X'
        
# checks for winner 
def check_winner(board, letter):
    for combo in winningCombinations:
        if all(board[i] == letter for i in combo):
            display_board(board)
            print (letter +' wins!\n')
            return True
    return False

# checks for draw if board is full
def board_full(board):
    return '-' not in board

# Displays the board
def display_board(board):
    print (f'{board[0]} | {board[1]} | {board[2]}\n{board[3]} | {board[4]} | {board[5]}\n{board[6]} | {board[7]} | {board[8]}' )

# player vs player game
def play_player():
    game_arr = ['-'] * 9
    letter = 'X'
    clear_screen()
    while (True):
        display_board(game_arr)
        try:
            user_choice = int(input("Please choose a spot from 1-9: "))
            if 1 <= user_choice <= 9 and game_arr[user_choice - 1] == '-':
                letter = user_turn(user_choice, game_arr, letter)
            else:
                print("Please pick a number between 1 and 9!")
        except ValueError:
            print("Invalid input. Please enter a number!")

        if check_winner(game_arr,'X') == True:break
        elif check_winner(game_arr,'O') == True:break

        elif board_full(game_arr):
            display_board(game_arr)
            print ('It is a Draw!\n')
            break

def cpu_make_move(board):
    #checks to win
    for i in range(9):
        if board[i] == '-':
            board[i] = 'O'
            if check_winner(board,'O') :
                return i
            board[i] = '-'

    # check to block
    for i in range(9):
        if board[i] == '-':
            board[i] = 'X'
            if check_winner(board,'X') :
                print('this will make me lose beep boop')
                return i
            board[i] = '-'
    empty_cells = [i for i in range(9) if board[i] == '-']
    return random.choice(empty_cells)

def play_cpu():
    game_arr = ['-'] * 9
    letter = 'X'
    # clear_screen()
    while (True):
        display_board(game_arr)
        try:
            user_choice = int(input("Please choose a spot from 1-9: "))
            if 1 <= user_choice <= 9 and game_arr[user_choice - 1] == '-':
                user_turn(user_choice, game_arr, letter)
            else:
                print("Please pick a number between 1 and 9!")
        except ValueError:
            print("Invalid input. Please enter a number!")
        
        if check_winner(game_arr,'X') == True:break
        
        if board_full(game_arr):
            display_board(game_arr)
            print ('It is a Draw!\n')
            break
        
        game_arr[cpu_make_move(game_arr)] = 'O'
        if check_winner(game_arr,'O') == True:break

        if board_full(game_arr):
            display_board(game_arr)
            print ('It is a Draw!\n')
            break


# Main Program
def main():
    clear_screen()
    while(True):
        menu()
        user_choice = Actions(int(input()))
        if user_choice == Actions.Exit:
            print("Goodbye")
            exit()
        elif user_choice == Actions.Player: play_player()
        elif user_choice == Actions.CPU: play_cpu()
        else: print("Pick a valid choice")

# start of the program
while __name__ == "__main__":
    main()