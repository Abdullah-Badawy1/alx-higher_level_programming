#!/usr/bin/python3
"""
Module 101-nqueens provides a solution to the N queens puzzle using an
iterative approach with enhanced efficiency and readability. The program finds
all possible solutions, including translations and reflections, for the N queens
puzzle.

Attributes:
    N (int): Number of queens and the size of the chessboard.
    solutions (list): A list containing all valid board configurations.

"""

from sys import argv

# Validating the command line arguments
if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    N = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if N < 4:
    print('N must be at least 4')
    exit(1)


def is_safe(board, row, col):
    """
    Checks if a queen can be placed at the given position without conflicts.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check for conflicts in the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check for conflicts along the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check for conflicts along the lower-left diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_nqueens(col, board, solutions):
    """
    Recursive function to solve the N queens puzzle.

    Args:
        col (int): The current column to place a queen.
        board (list): The current state of the chessboard.
        solutions (list): The list to store successful configurations.

    """
    if col >= N:
        # Convert the board configuration to a list of queen coordinates
        solution = [(i, row.index(1)) for i, row in enumerate(board)]
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(col + 1, board, solutions)
            board[i][col] = 0  # Backtrack


# Initialize the chessboard
initial_board = [[0 for _ in range(N)] for _ in range(N)]
solutions = []

# Solve the N queens puzzle
solve_nqueens(0, initial_board, solutions)

# Print the solutions
for solution in solutions:
    print(solution)
