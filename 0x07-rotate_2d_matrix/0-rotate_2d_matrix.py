#!/usr/bin/python3
"""module for the function rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise"""
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]
