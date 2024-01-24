#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics """

from sys import stdin


status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
count = 0


def print_all():
    """function to print all"""
    print("File size:", total_file_size)
    for key, value in status_dict.items():
        if value:
            print("{}: {}".format(key, value))


try:
    for line in stdin:
        count += 1
        try:
            line = line.split(" ")
            status_code = int(line[7])
            file_size = int(line[8])
        except (IndexError, TypeError):
            continue
        status_dict[status_code] += 1
        total_file_size += file_size
        if count == 10:
            print_all()
            count = 0
    print_all()
except KeyboardInterrupt:
    print_all()
