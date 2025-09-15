# Tic-Tac-Toe with Unbeatable AI
import math
import random

# All possible winning lines (rows, columns, diagonals)
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6)               # diagonals
]

# To Print the board in a nice format
def show_board(board):
    def cell(i):
        return board[i] if board[i] != " " else str(i+1)
    print()
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print()

# Return a list of free positions
def get_free_positions(board):
    return [i for i, mark in enumerate(board) if mark == " "]

# Check if a player has won
def check_winner(board, player):
    return any(all(board[pos] == player for pos in line) for line in WIN_LINES)

# Check if board is full
def board_full(board):
    return all(cell != " " for cell in board)

# Evaluate the board for minimax
def score_board(board, ai, human, depth):
    if check_winner(board, ai):
        return 10 - depth  # quicker wins are better
    if check_winner(board, human):
        return depth - 10  # slower losses are slightly better
    return 0  # draw

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, maximizing, alpha, beta, ai, human):
    score = score_board(board, ai, human, depth)
    if score != 0 or board_full(board):
        return score

    if maximizing:  # AI's turn
        best_score = -math.inf
        for move in get_free_positions(board):
            board[move] = ai
            val = minimax(board, depth+1, False, alpha, beta, ai, human)
            board[move] = " "
            best_score = max(best_score, val)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # pruning
        return best_score
    else:  # Human's turn
        best_score = math.inf
        for move in get_free_positions(board):
            board[move] = human
            val = minimax(board, depth+1, True, alpha, beta, ai, human)
            board[move] = " "
            best_score = min(best_score, val)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

# Pick the best move for the AI
def best_ai_move(board, ai, human):
    best_value = -math.inf
    choices = []
    for move in get_free_positions(board):
        board[move] = ai
        move_value = minimax(board, 0, False, -math.inf, math.inf, ai, human)
        board[move] = " "
        if move_value > best_value:
            best_value = move_value
            choices = [move]
        elif move_value == best_value:
            choices.append(move)
    return random.choice(choices) if choices else None

# Human player's move
def human_move(board, human):
    free = get_free_positions(board)
    while True:
        try:
            choice = input(f"Enter your move ({', '.join(str(p+1) for p in free)}): ")
            if choice.lower() in ("q", "quit", "exit"):
                print("Game ended by user.")
                exit()
            pos = int(choice) - 1
            if pos in free:
                board[pos] = human
                break
            else:
                print("Invalid move! Cell is occupied or out of range.")
        except ValueError:
            print("Please type a number between 1–9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe with AI 🤖")
    human = ""
    while human not in ("X", "O"):
        human = input("Do you want to be X or O? ").upper()
    ai = "O" if human == "X" else "X"

    first = ""
    while first not in ("1", "2"):
        first = input("Who plays first? (1) You  (2) AI: ")
    human_first = (first == "1")

    board = [" "] * 9
    turn_human = human_first

    show_board(board)

    while True:
        if turn_human:
            human_move(board, human)
        else:
            print("AI is thinking...")
            move = best_ai_move(board, ai, human)
            board[move] = ai
            print(f"AI chooses position {move+1}")

        show_board(board)

        # Check game status
        if check_winner(board, human):
            print("🎉 You win!")
            break
        if check_winner(board, ai):
            print("😎 AI wins!")
            break
        if board_full(board):
            print("🤝It's a draw!")
            break

        turn_human = not turn_human

    print("❌️Game over❌️.")

# Run the game
if __name__ == "__main__":
    play_game()
