# ecg_analysis.py


import json
import sys


def import_name():
    filename = sys.argv[1]
    return filename


def import_data(filename):
    pass


def string_split(string):
    output = string.split(",")
    return output


if __name__ == '__main__':
    filename = import_name()
