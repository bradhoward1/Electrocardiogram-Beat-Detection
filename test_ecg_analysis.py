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
