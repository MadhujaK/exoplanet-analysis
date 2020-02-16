from Exoplanet import Exoplanet
class TestInput(Exoplanet):
  def __init__(self):
    maxStarT= 0
    self.hotStarP = ''
    self.noStarPlanets= 0
    self.jsonData = {}
    self.radiusYear = {}
    self.timeline = {}

  def checkInput(self,args):
    ##code for handling invalid json
    for filePath in args.test:
      with open(filePath, 'r') as f:
        try:
          self.jsonData = json.load(f)
        except json.JSONDecodeError as j:
          print("Invalid json")
          os._exit(1)

  def runTestJson(self,args):
    for obj in self.jsonData:
      s = self.getOrphans(obj)
      if (s=="string"):
        continue
      self.getHottestStar(obj)
      r = self.validateValues(obj)
      if (r=="string"):
        continue
      self.getTimeline(obj)
      self.organizeTimeline()
      self.printInfo()


#----Main Program Starts Here ----
if __name__ == '__main__':
  import argparse
  import json
  import requests
  import os
  #parse path for tests
  parser = argparse.ArgumentParser(description='Processes Exoplanet Data')
  parser.add_argument('-t', '--test', metavar='file_path', type=str, nargs='+',
                   help='provide test input json file paths')
  args = parser.parse_args()
  exoplanet = Exoplanet()
  testInput = TestInput()
  if (args.test != None):
    testInput.checkInput(args)
    testInput.runTestJson(args)
  #if test argument not given run program to take input from url
  else:
    exoplanet.runLoop()
    exoplanet.organizeTimeline()
    exoplanet.printInfo()

