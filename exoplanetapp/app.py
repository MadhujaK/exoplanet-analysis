from flask import Flask
import argparse
from Exoplanet import Exoplanet
from TestInput import TestInput
app = Flask(__name__)

exoplanet = Exoplanet()
testInput = TestInput()

@app.route("/")
def index():
  #parse path for tests
  parser = argparse.ArgumentParser(description='Processes Exoplanet Data')
  parser.add_argument('-t', '--test', metavar='file_path', type=str, nargs='+',
                   help='provide test input json file paths')
  args = parser.parse_args()

  if (args.test != None):
    testInput.checkInput(args)
    testInput.runTestJson(args)
  #if test argument not given run program to take input from url
  else:
    exoplanet.runLoop()
    exoplanet.organizeTimeline()
    exoplanet.printInfo()
    return """
    <p>Hi I am running now!</p>
    <p>You can go view the various Exoplanet analysis on the following path:</p>
    <p>/orphans: Number of Orphan Planets</p>
    <p>/htp: The Hottest Star Planet</p>
    <p>/timeline: Written information about discovery of planets</p>
    <p>/chart(not available): graphical information about discovery of planets</p>
    """

@app.route("/orphans")
def orphanstar():
  return exoplanet.printOrphans()

@app.route("/htp")
def hotstarp():
  return exoplanet.printHotStarP()

@app.route("/timeline")
def timeline():
  return exoplanet.printTimeline()

#@app.route("/chart")
#def display():
#  return exoplanet.displayTimeline()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
