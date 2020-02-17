import unittest
import os
import json
import requests

class TestExoplanet(unittest.TestCase):
  def setUp(self):
    #initialize variables
    maxStarT= 0
    self.hotStarP = ''
    self.noStarPlanets= 0
    self.radiusYear = {}
    self.timeline = {}
    self.jsonData = {}
    self.radiusJpt = ''
    self.hostStarTemp = ''
    self.discoveryYear = ''

  def getJson(self):
    #if test arg not given get json data from url
    url = "https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets"
    try:
      r = requests.get(url)
    except:
      print("Error while retrieving data from url: "+ url)
      os._exit(1)
    try:
      self.jsonData = r.json()
    except:
      print("Invalid json")
      os._exit()
    try:
      self.radiusJpt = self.json["RadiusJpt"]
      self.discoveryYear = self.json["DiscoveryYear"]
      self.hotStarTemp = self.json["HotStarTempK"]
    except:
      pass


  def runLoop(self):
    #json processing loop
    self.getJson()
    for obj in self.jsonData:
      s = self.getOrphans(obj)
      if (s=="string"):
        continue
      self.getHottestStar(obj)
      r = self.validateValues(obj)
      if (r=="string"):
        continue
      self.getTimeline(obj)

  def validateValues(self,obj):
    #if either DiscoveryYear or Radius not present move on to next object
    try:
      int(obj["DiscoveryYear"])
      int(obj["RadiusJpt"])
    except:
      return "string"

  def getOrphans(self,obj):
    try:
      int(obj["HostStarTempK"])
    except:
      try:
        if (obj["HostStarTempK"]==""):
          self.noStarPlanets +=1
      except:
        pass
      return "string"

  def getOrphans(self,obj):
    try:
      int(obj["HostStarTempK"])
    except:
      try:
        if (obj["HostStarTempK"]==""):
          self.noStarPlanets +=1
      except:
        pass
      return "string"

  def getHottestStar(self,obj):
    try:
      #outer try checks if HostStarTemp key is present and integer
      #finds the planet with maximum temperature of host star
      if (obj["HostStarTempK"] > maxStarT):
        maxStarT = obj["HostStarTempK"]
        try:
          self.hotStarP = obj["PlanetIdentifier"]
        except:
          pass
    except:
       pass

  def getTimeline(self,obj):
    #store a dictionary of years with count of S, M and L as separate values attached to different keys
    if (obj["RadiusJpt"] == ''):
      pass
    elif (obj["RadiusJpt"] < 1):
      try:
        self.radiusYear[str(obj["DiscoveryYear"])+"S"]+=1
      except:
        self.radiusYear[str(obj["DiscoveryYear"])+"S"]=1
    elif (obj["RadiusJpt"] < 2):
      try:
        self.radiusYear[str(obj["DiscoveryYear"])+"M"]+=1
      except:
        self.radiusYear[str(obj["DiscoveryYear"])+"M"]=1
    else:
      try:
        self.radiusYear[str(obj["DiscoveryYear"])+"L"]+=1
      except:
        self.radiusYear[str(obj["DiscoveryYear"])+"L"]=1


  def organizeTimeline(self):
    for item in self.radiusYear:
      try:
        #strip the S, M and L from <year>
        [s,m,l] = self.timeline[int(item[0:4])]
      except:
        [s,m,l] = [0,0,0]
      #store a list [small,medium,large] for each year
      if (item[4] == "S"):
        [s,m,l] = [self.radiusYear[item],m,l]
      if (item[4] == "M"):
        [s,m,l] = [s,self.radiusYear[item],l]
      if (item[4] == "L"):
        [s,m,l] = [s,m,self.radiusYear[item]]
      self.timeline[int(item[0:4])] = [s,m,l]

  def printInfo(self):
      print("Number of planets without stars:" + str(self.noStarPlanets))
      print("Hottest Star:" + self.hotStarP)
      print("Timeline: ")
      #sort and print timeline here
      for (year,radii) in sorted(self.timeline.items()):
        print("In %s we discovered %s small planets, %s medium planets, and %s large planets" % (year,self.timeline[int(year)][0],timeline[int(year)][1],self.timeline[int(year)][2]))

  def test_starTemp_int(self):
    self.runLoop()
    try:
      self.assertEqual(type(self.hostStarTemp), 'int' , "Star temp is not an integer")
    except:
      self.assertEqual(self.hostStarTemp, '', "Star temp is not an integer or empty")


  def test_radiusJpt_int(self):
    self.runLoop()
    try:
      self.assertEqual(type(self.radiusJpt), 'int' , "Radius is not an integer")
    except:
      self.assertEqual(self.radiusJpt, '', "Radius is not an integer or empty")

  def test_discoverYear_int(self):
    self.runLoop()
    try:
      self.assertEqual(type(self.radiusJpt), 'int' , "Discovery year is not an integer")
    except:
      self.assertEqual(self.radiusJpt, '', "Discovery year is not an integer or empty")


if __name__ == '__main__':
    unittest.main()
