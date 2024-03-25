#!/usr/bin/python3

import sys


def print_statistics(dictionary, final_size):
    """
    Prints file size and status code statistics.
    Args:
        dictionary: Dictionary containing status code counts.
        final_size: Total file size.
    Returns:
        None
    """
    print("File size: {}".format(final_size))
    for key, val in sorted(dictionary.items()):
        if val != 0:
            print("{}: {}".format(key, val))


final_size = 0
code = 0
length = 0
dictionary = {"200": 0,
              "301": 0,
              "400": 0,
              "401": 0,
              "403": 0,
              "404": 0,
              "405": 0,
              "500": 0}

try:
    for line in sys.stdin:
        parsed = line.split()
        parsed = parsed[::-1]

        if len(parsed) > 2:
            length += 1

            if length <= 10:
                final_size += int(parsed[0])
                code = parsed[1]

                if code in dictionary.keys():
                    dictionary[code] += 1

            if length == 10:
                print_statistics(dictionary, final_size)
                length = 0

finally:
    print_statistics(dictionary, final_size)
