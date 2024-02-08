#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard. Write a program that solves the N queens problem.
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = []
for i in range(N):
    row = []
    for y in range(N):
        row.append(0)
    board.append(row)
queens = []


def available_spots(queens, board):
    """Check and mark available spots on a chessboard."""
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            for x, y in queens:
                if i == x or j == y or abs(i - x) == abs(j - y):
                    board[i][j] = 1


def queen_down(N, queens, board, final_combo):
    """
    Place queens on a chessboard of size N,
    exploring all combinations and returning unique solutions.
    """
    if len(queens) == N:
        sorted_queens = sorted(queens, key=lambda x: x[0])
        if sorted_queens not in final_combo:
            final_combo.append(queens)
        return final_combo
    available_spots(queens, board)
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if not square:
                board_cpy = [r[:] for r in board]
                queen_down(N, queens + [[i, j]], board_cpy, final_combo)
    return final_combo


queens = queen_down(N, queens, board, [])
for queen in queens:
    print(queen)
