N=8 # Size of the board

def print_solution(board):
    # Prints the chessboard configuration
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col):
    # Checks if it's safe to place a queen at board[row][col].
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
            
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
            
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False
            
    return True # Safe placement

def solve_n_queens(board, row):
    # Solves the N-Queens problem using backtracking.
    if row == N:
        print_solution(board) # Print valid board configuration
        return True # Solution found
        
    for col in range(N): # Try placing queen in each column
        if is_safe(board, row, col):
            board[row][col] = 1 # Place the queen
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0 # Backtrack if not a solution
            
    return False # No valid placement found

# Initialize an 8x8 chessboard (0 represents empty, 1 represents a queen)
chess_board = [[0] * N for _ in range(N)]
solve_n_queens(chess_board, 0)
