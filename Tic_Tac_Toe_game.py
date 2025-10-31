import random

board = [' ' for _ in range(9)]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(symbol):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(board[a] == board[b] == board[c] == symbol for a,b,c in win_combinations)

def is_full():
    return ' ' not in board

def user_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)-1] == ' ':
            board[int(move)-1] = 'X'
            break
        else:
            print("Invalid move! Try again.")

def computer_move():
    available = [i for i, spot in enumerate(board) if spot == ' ']
    move = random.choice(available)
    board[move] = 'O'
    print(f"Computer chose position {move+1}")

def play_game():
    print("Welcome to Tic Tac Toe! 🎮")
    print("You are 'X' and Computer is 'O'")
    print_board()

    while True:
        user_move()
        print_board()
        if check_winner('X'):
            print("🎉 Congratulations! You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        computer_move()
        print_board()
        if check_winner('O'):
            print("💻 Computer wins! Better luck next time.")
            break
        if is_full():
            print("It's a draw!")
            break

# Run the game
play_game()
