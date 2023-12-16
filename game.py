import random
import tkinter as tk
import tkinter.messagebox as messagebox

# winning combinations for tic tac toe
winningCombinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
]

# creating my gui!

    #main menu
def open_main_menu():        
    main_menu_window = tk.Toplevel(root)
    main_menu_window.geometry("1280x720")
    main_menu_window.title("Tic Tac Toe")

    main_menu_frame = tk.Frame(main_menu_window)
    main_menu_frame.pack()

    label = tk.Label(main_menu_frame, text="Tic Tac Toe", font=("Helvetica", 16))
    label.pack(pady=20)

    # Button options
    options = ["Player vs Player", "Player vs CPU", "Exit"]
    for option in options:
        button = tk.Button(main_menu_frame, text=option, width=20, height=2, command=lambda opt=option: on_option_selected(opt, main_menu_window))
        button.pack(pady=50)

    main_menu_window.mainloop()

def on_option_selected(option, main_menu_window):
    if option == "Player vs Player":
        print("Player vs Player selected")
        open_game_window("Player vs Player", main_menu_window)
    elif option == "Player vs CPU":
        print("Player vs CPU selected")
        open_game_window("Player vs CPU", main_menu_window)
    elif option == "Exit":
        print("Exit selected")  
        root.destroy()


def open_game_window(game_mode,previous_window):
    previous_window.destroy()

    game_window = tk.Toplevel(root)
    game_window.geometry("1280x720")
    game_window.title("Game Window")

    def restart_game():
        # Reset the game state and hide the buttons and labels
        nonlocal game_arr, symbol
        game_arr = ['-'] * 9
        symbol[0] = 'X'
        result_label.config(text="")
        hide_end_game_buttons()

        # Reset button texts
        for i in range(3):
            for j in range(3):
                buttons[i][j].configure(text=" ")

    def back_to_menu():
        # Close the game window and show the main menu
        game_window.destroy()
        open_main_menu()

    def show_end_game_buttons(result):
        restart_button.grid(row=3, column=0, pady=10)
        menu_button.grid(row=3, column=1, pady=10)
        result_label.config(text=result)

    def hide_end_game_buttons():
        restart_button.grid_forget()
        menu_button.grid_forget()

    # checks for draw if board is full
    def check_draw(board):
        if '-' not in board:
            result = ("It's a Draw")
            show_end_game_buttons(result)

        # checks for winner 
    def check_winner(board, symbol):
        for combo in winningCombinations:
            if all(board[i] == symbol for i in combo):
                print (symbol[0] +' wins!\n')
                return True
        return False

    def on_square_click_player(row, col, symbol,game_arr,buttons):
        if game_arr[row * 3 +col] == '-':
            game_arr[row * 3 +col] = symbol[0]
            buttons[row][col].configure(text=symbol[0])

            if check_winner(game_arr,symbol[0]):
                result = (f"{symbol[0]} Wins!")
                show_end_game_buttons(result)

            check_draw(game_arr)

            # changing turn
            if symbol[0] == 'X':
                symbol[0] = 'O'
            else: 
                symbol[0] = 'X'

    def cpu_make_move(board,buttons):
     #checks to win
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O'
                if check_winner(board,'O') :
                    row, col = divmod(i, 3)
                    buttons[row][col].configure(text='O')
                    return
                board[i] = '-'

        # check to block
        for i in range(9):
            if board[i] == '-':
                board[i] = 'X'
                if check_winner(board,'X') :
                    board[i] = 'O'
                    row, col = divmod(i, 3)
                    buttons[row][col].configure(text='O')
                    return
                board[i] = '-'
                
        empty_cells = [i for i in range(9) if board[i] == '-']
        if empty_cells:
            random_index = random.choice(empty_cells)
            row, col = divmod(random_index, 3)
            buttons[row][col].configure(text='O')
            game_arr[random_index] = 'O'

    
    def on_square_click_cpu(row, col, symbol,game_arr,buttons):
        if game_arr[row * 3 +col] == '-':
            game_arr[row * 3 +col] = symbol[0]
            buttons[row][col].configure(text=symbol[0])

            if check_winner(game_arr,symbol[0]):
                result = "You Win!"
                show_end_game_buttons(result)

            check_draw(game_arr)

            #cpu turn
            cpu_make_move(game_arr,buttons)
            if check_winner(game_arr,'O'):
                result = "Computer Wins!"
                show_end_game_buttons(result)
            
            check_draw(game_arr)
            
    # declaring all the game variables
    symbol = ['X']
    game_arr = ['-'] * 9

    buttons = []

    for i in range(3):
        row_buttons = []
        for j in range(3):
            if game_mode == "Player vs CPU":
                button = tk.Button(game_window, text=" ", width=10, height=4,padx=5, command=lambda r=i, c=j: on_square_click_cpu(r, c, symbol, game_arr, buttons))
            elif game_mode == "Player vs Player":
                button = tk.Button(game_window, text=" ", width=10, height=4,padx=5, command=lambda r=i, c=j: on_square_click_player(r, c, symbol, game_arr, buttons))
           
            button.grid(row=i, column=j)
            row_buttons.append(button)
        buttons.append(row_buttons)

    restart_button = tk.Button(game_window, text="Restart", command=restart_game)
    menu_button = tk.Button(game_window, text="Back to Menu", command=back_to_menu)
    result_label = tk.Label(game_window, text="", font=("Helvetica", 16))

    result_label.grid(row=3, column=2, columnspan=2, pady=20)

    game_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    open_main_menu()  
    root.mainloop()  