# ecg_analysis.py


import json
import sys
import logging
import math


def import_name():
    filename = sys.argv[1]
    return filename


def import_data(filename):
    contents = list()
    with open(filename, 'r') as input_file:
        file = input_file.readlines()
        for line in file:
            contents.append(line.strip("\n"))
        return contents


def string_split(string):
    output = string.split(",")
    return output


def str_to_float(input_results):
    data = list()
    for i in input_results:
        try:
            i = float(i)
        except ValueError:
            logging.error("This line of data is not usable: line skipped")
        data.append(i)
    return data


def float_check(nums):
    result = all(isinstance(n, float) for n in nums)
    return result


def line_manip(contents):
    time = list()
    voltage = list()
    for line in contents:
        line = string_split(line)
        data = str_to_float(line)
        if float_check(data) is False:
            continue
        elif len(data) != 2:
            continue
        elif math.isnan(data[1]) is True or math.isnan(data[0]) is True:
            logging.error("This line of data is not usable: line skipped")
            continue
        else:
            time.append(data[0])
            voltage.append(data[1])
    return time, voltage


def norm_range(voltage):
    result = all(elem >= -300.0 and elem <= 300.0 for elem in voltage)
    if result is False:
        logging.warning('The voltage data contains an element outside'
                        ' of the normal range of +/- 300 mV')
    return result


if __name__ == '__main__':
    logging.basicConfig(filename="my_code.log", filemode='w',
                        level=logging.DEBUG)
    logging.info("--------New Run--------\n")
    filename = import_name()
    contents = import_data(filename)
    time, voltage = line_manip(contents)
    print(time)
    print(voltage)
    logging.info("********End of Run********\n")
