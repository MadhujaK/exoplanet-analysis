This software downloads structured data from a url and analyses the objects to find correlation in the data

It prints out the number of orphan planets i.e. with no host stars
It prints out the name of the planet with the hottest host star
A timeline of number of small, medium and large planets in a certain year


to run the app run command:

git clone <name_of repo>
cd exoplanet-analysis
python3 exoApp.py

to run tests give the parameter test while running the app
python3 exoApp.py -h

Output should be something like:
usage: exoApp.py [-h] [-t file_path [file_path ...]]

Processes Exoplanet Data

optional arguments:
  -h, --help            show this help message and exit
  -t file_path [file_path ...], --test file_path [file_path ...]
                        provide test input json file paths


this shows you how to use the test files
test files are json data files included in the tests/inputData folder

To run a test to check how the software reacts to invalid json data, run the invalid.json test
~/exoplanet-analysis$ cd tests/inputData
~/exoplanet-analysis/tests/inputData$ ls
invalid.json  invalidKey.json  invalidValue.json

This should give you a list of test data
