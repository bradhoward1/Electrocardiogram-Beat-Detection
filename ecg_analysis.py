# ecg_analysis.py


import json
import sys


def import_name():
    filename = sys.argv[1]
    return filename


def import_data(filename):
    time = list()
    voltage = list()
    with open(filename, 'r') as input_file:
        file = input_file.readlines()
        for line in file:
            line = line.strip("\n")
            output = string_split(line)
            output = str_to_float(output)
            time.append(output[0])
            voltage.append(output[1])
        return time, voltage


def string_split(string):
    output = string.split(",")
    return output


def str_to_float(input_results):
    data = list()
    for i in input_results:
        try:
            i = float(i)
        except ValueError:
            print("Not a convertable string")
        data.append(i)
    return data


def float_check(nums):
    result = all(isinstance(n, float) for n in nums)
    return result


if __name__ == '__main__':
    filename = import_name()
