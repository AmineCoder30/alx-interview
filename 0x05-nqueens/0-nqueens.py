#!/usr/bin/python3
""" A program that solves the N queens problem
"""
from sys import argv


def check_row(board, index, board_len):
    """ Check if there is a queen in the row """
    for r in range(board_len):
        if board[index][r]:
            return (False)

    return (True)


def check_r_angle(board, row, col, board_len):
    """ Check if there is a queen in the left angle """
    c = col
    for r in range(row, -1, -1):
        if c >= board_len:
            break
        if board[r][c]:
            return (False)
        c += 1

    c = col
    for r in range(row, board_len):
        if c < 0:
            break
        if board[r][c]:
            return (False)
        c -= 1

    return (True)


def check_l_angle(board, row, col, board_len):
    """ Check if there is a queen in the right angle """
    c = col
    for r in range(row, -1, -1):
        if c < 0:
            break
        if board[r][c]:
            return (False)
        c -= 1

    c = col
    for r in range(row, board_len):
        if c >= board_len:
            break
        if board[r][c]:
            return (False)
        c += 1

    return (True)


def chek_all(board, r, c, n):
    if not check_row(board, r, n):
        return (False)

    if not check_l_angle(board, r, c, n):
        return (False)

    return (check_r_angle(board, r, c, n))


def main():
    """ The Main Function """

    argc = len(argv)
    if argc != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except Exception:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    n_range = range(n)
    i = 0
    c = 0
    r = i
    board = [[0 for _ in n_range] for _ in n_range]
    result = []
    while i < n:
        while (c < n):
            found = 0

            while (r < n):
                if chek_all(board, r, c, n):
                    board[r][c] = 1
                    result.append([c, r])
                    found = 1
                    r = 0
                    break
                r += 1

            if not found and len(result):
                last_i = result.pop()
                c = last_i[0]
                r = last_i[1] + 1
                board[last_i[1]][last_i[0]] = 0
                continue
            c += 1

        if len(result):
            print(result)
            i = result[0][1]
            last_i = result.pop()
            c = last_i[0]
            r = last_i[1] + 1
            board[last_i[1]][last_i[0]] = 0
        else:
            return


if __name__ == "__main__":
    main()
