# ECG Analysis Assignment

This README.md file provides an in-depth look at the `ecg_analysis.py` file, including how to run it and other important aspects. The information is provided below.

## Instructions

### Running the Program

The `ecg_analysis.py` file must be run through the command terminal. Before running the code, first ensure that you have established a virtual environment in Python and that all of the packages mentioned in the `requirements.txt` file are installed as well.
From the command line, utilize the following format when running the program:

`python3 ecg_analysis.py test_data1.csv`

This format is necessary to ensure that
1. the proper test file is read in
2. the proper name is given to the outputted JSON file

IT IS ESSENTIAL THAT THE TEST FILES ARE IN THE SAME DIRECTORY AS THE PROGRAM ITSELF. The code will not generate the correct JSON file nor will it output the information in the correct location if the exact format is not followed above. So, to ensure proper formatting, put the test files into the same directory as the `ecg_analysis.py` file.

Once the code is run with the format mentioned above, two files will be outputted: one file titled `my_code.log` which provides a log of all errors, warnings and other important information to the user. Furthermore, the other file outputted is the JSON file including the dictionary of all the calculated metrics. This JSON file will have the same name as the test file. For example, if the line above were run in the command line, the outputted JSON file would have the name `test_data1.json`.

Ultimately, this code will have the user input a file name into the command line and will return a dictionary of the following metrics in a JSON file:

    - `duration`: time duration of the ECG strip
    - `voltage_extremes`: tuple in the form `(min, max)` where `min` and `max`
    are the minimum and maximum lead voltages found in the data file.      
    - `num_beats`: number of detected beats in the strip, as a numeric variable type.
    - `mean_hr_bpm`: estimated average heart rate over the length of the strip  
    - `beats`: list of times when a beat occurred

### Defining a Beat

To define a beat in this code, a Python package was installed. This Python package scipy.signal, and the specific function necessary for this analysis is called `find_peaks`. Literature online states that this function "takes a one-dimensional array and finds all local maxima by simple comparison of neighbouring values. Optionally, a subset of these peaks can be selected by specifying conditions for a peak’s properties".
(https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html)

This function compares neighboring values to each other to determine any local maxima. Within the function, it states that one of the parameters that you can change is the expected distance between the peaks. I decided to choose 190 data points as my approximate distance because as I tested the files, this parameter seemed to be the most accurate. The combination of setting an approximate distance between peaks and comparing neighboring values allows us to determine the peaks of the ECG data. The way that this information is presented is through the returning of a list of indices which correlate to the indices at which the voltage maxima occurred. Thus, by reading in the list of voltage values, the `find_peaks()` function is able to present the user with a list of the correlating indices at which the peaks occurred.

### Calculating Beats per Minute

The `find_peaks()` function returns a list of indices telling the user where in the list of voltage values the peaks actually occurred. The length of this list of indices can be used to determine how many peaks were actually found. So, if the length of the list of indices is 35, then that means that the `find_peaks()` function found 35 total peaks in the ECG strip. Furthermore, one of the pieces of data that we were asked to determine was the time duration of the ECG strip. Using the number of determined peaks along with the time duration of the ECG strip, the average heart rate in beats per minute can be found. The following formula is used:

Average Heart Rate = (# beats in strip / # seconds strip lasts) * (60 seconds / 1 minute)

By multiplying by 60, we can convert the average heart rate from average beats per second to average beats per minute, which is a much more understandable and acceptable value.

## License

MIT License

Copyright (c) [2020] [Bradley Howard]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

