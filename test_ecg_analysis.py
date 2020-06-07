# test_ecg_analysis.py


import pytest


@pytest.mark.parametrize("result, expected",
                         [("0.003,0.30983", ["0.003", "0.30983"]),
                          ("0.45", ["0.45"]),
                          ("word,0.9", ["word", "0.9"]),
                          ("NaN,0.10", ["NaN", "0.10"])])
def test_string_split(result, expected):
    from ecg_analysis import string_split
    answer = string_split(result)
    assert answer == expected


@pytest.mark.parametrize("result, expected",
                         [(["8", "0.9"], [8, 0.9]),
                          (["word", "0.9"], ["word", 0.9]),
                          (["word"], ["word"]),
                          (["8"], [8])])
def test_str_to_float(result, expected):
    from ecg_analysis import str_to_float
    answer = str_to_float(result)
    assert answer == expected


@pytest.mark.parametrize("result, expected",
                         [(["dope", 9], False),
                          ([9.2, 0.2], True),
                          (["dope"], False)])
def test_float_check(result, expected):
    from ecg_analysis import float_check
    answer = float_check(result)
    assert answer == expected


def test_line_manip_time():
    from ecg_analysis import line_manip
    contents = ["8,2.0\n", "word,3\n", "word\n", "8\n", "2,3\n"]
    expected_time = [8.0, 2.0]
    time, voltage = line_manip(contents)
    assert time == expected_time


def test_line_manip_voltage():
    from ecg_analysis import line_manip
    contents = ["8,2.0\n", "word,3\n", "word\n", "8\n", "2,3\n"]
    expected_voltage = [2.0, 3.0]
    time, voltage = line_manip(contents)
    assert voltage == expected_voltage
