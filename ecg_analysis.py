# ecg_analysis.py


import json
import sys


def import_name():
    filename = sys.argv[1]
    return filename


def import_data(filename):
    contents = list()
    with open(filename, 'r') as input_file:
        file = input_file.readlines()
        for line in file:
            line = line.strip("\n")
            output = string_split(line)
            output = str_to_float(output)
            contents.append(output)
        return contents


def str_to_float(input_results):
    data = list()
    for i in input_results:
        try:
            i = float(i)
        except ValueError:
            print("Not a convertable string")
        data.append(i)
    return data


def string_split(string):
    output = string.split(",")
    return output


if __name__ == '__main__':
    filename = import_name()
