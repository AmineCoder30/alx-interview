#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics

    Input format:
        <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
            <status code> <file size>
        (if the format is not this one, the line must be skipped)

    format: <status code>: <number>
"""
import sys
import re


def print_status(total_size, status_codes):
    """ Print Status Function """
    print(f"File size: {total_size}")
    sort_codes = sorted(status_codes.items())
    for code, count in sort_codes:
        print(f"{code}: {count}")


def match_input(input_line):
    """ Check if input line match """
    data = {'status_code': 0, 'file_size': 0}

    pattern = re.compile(r'\b^[0-9]+.[0-9]+.[0-9]+.[0-9]+ - '
                         r'\[[0-9]+-[0-9]+-[0-9]+ '
                         r'[0-9]+:[0-9]+:[0-9]+.[0-9]+\] '
                         r'"GET \/projects\/260 HTTP\/1.1" '
                         r'(200|301|400|401|403|404|405|500) ([0-9]+)$\b')

    match = pattern.search(input_line)
    if not match:
        return (None)

    data['status_code'] = match.group(1)
    data['file_size'] = int(match.group(2))
    return (data)


def main():
    """ Main Function """
    total_size = 0
    status_codes = {}
    counter = 0

    try:
        while True:
            line = input()
            data = match_input(line)

            if not data:
                continue

            counter += 1
            total_size += data['file_size']
            status_code = data['status_code']

            if not status_codes.get(status_code, None):
                status_codes[status_code] = 1
            else:
                status_codes[status_code] += 1

            if counter % 10 == 0:
                print_status(total_size, status_codes)
                status_codes = {}
    except (KeyboardInterrupt, EOFError):
        print_status(total_size, status_codes)


if __name__ == "__main__":
    main()
