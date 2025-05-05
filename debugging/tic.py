#!/usr/bin/python3

def print_board(board):
    """Display the current game board."""
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Don't print horizontal line after the last row
            print("-" * 9)

def check_winner(board):
    """Check if there is a winner."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """Check if the board is full (tie game)."""
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt, valid_range):
    """Get valid integer input from user within the specified range."""
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Input must be one of {list(valid_range)}. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def tic_tac_toe():
    """Main game function for Tic-Tac-Toe."""
    print("Welcome to Tic-Tac-Toe!")
    print("Player X goes first. Enter row and column (0-2) to place your mark.")
    
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    game_over = False
    
    while not game_over:
        print_board(board)
        
        # Get valid input from the current player
        print(f"\nPlayer {current_player}'s turn")
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {current_player}: ", range(3))
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {current_player}: ", range(3))
        
        # Make a move if the cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player
            
            # Check for winner after the move
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            # Check for tie after the move
            elif is_board_full(board):
                print_board(board)
                print("It's a tie! Game over.")
                game_over = True
            # Switch players
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    try:
        tic_tac_toe()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
