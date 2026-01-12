
import math

board = [" " for _ in range(9)]

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_board_full(board):
    return " " not in board

def get_valid_moves(board):
    return [i for i in range(9) if board[i] == " "]

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_valid_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_valid_moves(board):
            board[move] = "X"
            score = minimax(board, depth + 1, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in get_valid_moves(board):
        board[i] = "O"
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move

def play_game():
    print("Tic-Tac-Toe: You are X, AI is O")
    print_board(board)
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move, try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 8.")
            continue

        board[move] = "X"
        if is_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("Draw!")
            break

        ai_move = best_move(board)
        board[ai_move] = "O"
        print("\nAI plays:")
        print_board(board)
        if is_winner(board, "O"):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("Draw!")
            break

play_game()
