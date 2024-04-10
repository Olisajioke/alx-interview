#!/usr/bin/python3
"""Solves the N queens puzzle and prints every possible solution."""
import sys


def is_safe(board, row, col, N):
    """Check if there is a queen in the same column up to the current row"""
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, row, N):
    """Function that solves n_queens"""
    if row == N:
        print_solution(board, N)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens(board, row + 1, N)
            board[row][col] = 0


def print_solution(board, N):
    """function that prints"""
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append((i, j))
                break
    print(solution)


def nqueens(N):
    """function that solves N"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solve_n_queens(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
