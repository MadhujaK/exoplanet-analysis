##There is a directory called exoplanetapp that contains a more structured flask app for the same function
##It displays info on commandline and the web browser; with Dockerfile and Kubernetes yml for deployement included
##README for that included in the exoplanetapp/ folder

##this below, is a README for the command line version only

Description:
This software downloads structured data from a url and analyses the objects to find correlation in the data
Prints out the number of orphan planets i.e. with no host stars
Prints out the name of the planet with the hottest host star
Prints timeline of number of small, medium and large planets in a certain year


Basic Git cone usage:
to run the app run commands --

git clone <name_of repo>
cd exoplanet-analysis
python3 exoApp.py

to run with test inputs give the parameter test while running the app
Help parameter gives a list of options the software can take
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

To run a test input to check how the software reacts to invalid json data, run the invalid.json test
~/exoplanet-analysis$ cd tests/inputData
~/exoplanet-analysis/tests/inputData$ ls
invalid.json  invalidKey.json  invalidValue.json

This should now give you a list of test input files as above

Using with Docker:

1. install docker to your machine and give the user "docker" root permissions
2. clone the repo to local machine -- git clone <repo_path>
3. cd exoplanet-analysis/
4. build the docker image using the Dockerfile in current directory -- docker build -t exoplanet-app .
5. docker run exoplanet-app

This should output the software output stream on commandline


Timing the current script:
exoplanet-analysis/tests/time.py is a script added to the repo to time the exoApp.py script total runtime 

Testing for the script:
unit tests are located in the tests/unittest folder
to execute the testExo.py file with 3 unit tests included execute:

cd tests/unittest
python3 -m unittest -v testExo.py
