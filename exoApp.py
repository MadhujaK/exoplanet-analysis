def getJson():
  #if test arg not given get json data from url
  url = "https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets"
  try:
    r = requests.get(url)
  except:
    print("Error while retrieving data from url: "+ url)
    os._exit(1)
  return r.json()

def invTest(args):
  ##code for handling invalid json
  testPathList = args.test
  for Path in testPathList:
    with open(Path, 'r') as f:
      try:
        jsonData = json.load(f)
      except json.JSONDecodeError as j:
        print("Invalid json")
        os._exit(1)
  return jsonData

def timeline():
  #store a dictionary of years with count of S, M and L as separate values attached to different keys
  if (j["RadiusJpt"] == ''):
    pass
  elif (j["RadiusJpt"] < 1):
    try:
      radiusYear[str(j["DiscoveryYear"])+"S"]+=1
    except:
      radiusYear[str(j["DiscoveryYear"])+"S"]=1
  elif (j["RadiusJpt"] < 2):
    try:
      radiusYear[str(j["DiscoveryYear"])+"M"]+=1
    except:
      radiusYear[str(j["DiscoveryYear"])+"M"]=1
  else:
    try:
      radiusYear[str(j["DiscoveryYear"])+"L"]+=1
    except:
      radiusYear[str(j["DiscoveryYear"])+"L"]=1
  return radiusYear

def organizeTimeline():
  y = {}
  for item in radiusYear:
    try:
      #strip the S, M and L from <year>
      [s,m,l] = y[int(item[0:4])]
    except:
      [s,m,l] = [0,0,0]
    #store a list [small,medium,large] for each year
    if (item[4] == "S"):
      [s,m,l] = [radiusYear[item],m,l]
    if (item[4] == "M"):
      [s,m,l] = [s,radiusYear[item],l]
    if (item[4] == "L"):
      [s,m,l] = [s,m,radiusYear[item]]
    y[int(item[0:4])] = [s,m,l]
  return y

def printAll(noStarPlanets, hotStarP, yearPlanetList):
    print("Number of planets without stars:" + str(noStarPlanets))
    print("Hottest Star:" + hotStarP)
    print("Timeline: ")
    #sort and print timeline here
    for (year,radii) in sorted(yearPlanetList.items()):
      print("In %s we discovered %s small planets, %s medium planets, and %s large planets" % (year,yearPlanetList[int(year)][0],yearPlanetList[int(year)][1],yearPlanetList[int(year)][2]))


#----Main Program Starts Here ----
if __name__ == '__main__':
  import argparse
  import json
  import requests
  import os
  #initialize variables
  maxStarT= 0
  hotStarP = ''
  noStarPlanets= 0
  small , medium, large = ([] for i in range(3))
  radiusYear = {}
  #parse path for tests
  parser = argparse.ArgumentParser(description='Processes Exoplanet Data')
  parser.add_argument('-t', '--test', metavar='file_path', type=str, nargs='+',
                   help='provide test input json file paths')
  args = parser.parse_args()
  if (args.test != None):
    jsonData = invTest(args)
  #if test argument not given run program to take input from url
  else:
    jsonData = getJson()
  #json processing loop
  for j in jsonData:
  #check if HostStarTemp keys are present -- if not continue process
    try:
      #counts number of No Star Planets
      #finds the planet with maximum temperature of host star
      if (j["HostStarTempK"]==""):
        noStarPlanets +=1
      elif (j["HostStarTempK"] > maxStarT):
        maxStarT = j["HostStarTempK"]
        try:
          hotStarP = j["PlanetIdentifier"]
        except:
          pass
    except:
       pass
  #if either DiscoveryYear or Radius not present move on to next object
    try:
      check1 = j["DiscoveryYear"]
      check2 = j["RadiusJpt"]
    except:
      continue
    if (j["DiscoveryYear"] == ''):
      continue
    radiusYear = timeline()
  yearPlanetList = organizeTimeline()
  printAll(noStarPlanets,hotStarP,yearPlanetList)
