#COVID-19 Spread Through the Corps of Cadets
#Author: Madison Teague
#Last Updated: 9 February 2021

import random
#import numpy as np
#import math
import timeit
################################################################################
#Functions and cadet class
################################################################################

class Cadet():
  def __init__(self, year, immune, infTime, symp, knownInf):
    self.year = year #1 = cow/firstie, 2 = yuk/plebe
#    self.schedule = schedule
    self.immune = immune #attribute for immunity classification (0/1)
    self.infTime = infTime #attribute for known infection time (0-14)
    self.symp = symp #attribute for symptomatic state classification (0/1)
    self.knownInf = knownInf #attribute for when infection is identified(0/1)



#function for random variables from uniform random distribution
def random_v(x):
  rv = random.randrange(0,x,1)
  return(rv)

#random determination of symptoms
def sympRate():
  rv = random_v(100)
  if rv >= 20:
    return(0)
  else:
    return(1)

#function to create new infections, assigns a symptomatic condition
def newInfection(cadet):
  if cadet.immune == 1 or cadet.infTime != 0:
    pass
  else:
    cadet.symp = sympRate()
    cadet.knownInf = 1
    cadet.infTime = 1

#TP rate = .95
#FN rate = .05
#TN rate = .99
#FP rate = .01

#Test function
def test(cadet):
  if cadet.infTime >= 1:
    results = random_v(100)
    if results >= 5:
      cadet.knownInf = 1
      return("tP")
    else:
      return("fN")

  else:
    results = random_v(100)
    if results > 1:
       return ("tN")
    else:
      return("fP")

def disinfection(cadet):
    cadet.symp = 0
    cadet.knownInf = 0
    cadet.immune = 1
    cadet.infTime = 0



################################################################################
#Building Simulation Environment
################################################################################

teams = [[]]*45

companies = [[]]*36

#print(companies)

rooms = [[]]*1728


upper1 = [Cadet(1,0,0,0,0)]*2023 #totally succeptible cadet
upper2 = [Cadet(1,1,0,0,0)]*107  #Immune cadet
upper3 = [Cadet(1,1,1,0,0)]*46  #activley infected (asymptomatic)
upper4 = [Cadet(1,1,1,1,0)]*14   #activley infected (symptomatic)

under1 = [Cadet(2,0,0,0,0)]*2023
under2 = [Cadet(2,1,0,0,0)]*107
under3 = [Cadet(2,1,1,0,0)]*46
under4 = [Cadet(2,1,1,1,0)]*14

#print(type(upper1))
#4392 cadets (122 per company)
allupper = upper1 + upper2 + upper3 + upper4
random.shuffle(allupper)
allunder = under1 + under2 + under3 + under4
random.shuffle(allunder)
theCorps = allunder + allupper
random.shuffle(theCorps)

#print(len(theCorps))
#print((type(theCorps)))

def assignCompany(upper, under, compList):
  for c in compList:
    while len(c) < 61:
      if len(upper) > 0:
        cadet = upper.pop()
        c.append(cadet)
    while len(c) < 122:
      if len(under) > 0:
        cadet = under.pop()
        c.append(cadet)
  return compList

companies = assignCompany(allupper, allunder, companies)


def findCompany(cadet, compList):
  for c in compList:
    if cadet in c:
      return c


def assignTeam(corps, tmList):
  cadets = corps
  for team in tmList:
    while len(team) < 50:
      if len(cadets) > 0:
        cadet = cadets.pop(random_v(len(cadets)))
        team.append(cadet)
  return tmList

teams = assignTeam(theCorps, teams)

def findTeam(cadet, tmList):
  for t in tmList:
    if cadet in t:
      return t


def assignRoom(corps, compList, roomList):
  for i in range(36):
    upper = []
    under = []
    for cdt in compList[i]:
      if cdt.year == 1:
        upper.append(cdt)
      else:
        under.append(cdt)
    for room_under in roomList[(48*i):(48*i + 23)]:
      while len(room_under) < 3:
        if len(under) > 0:
          cadet = under.pop(random_v(len(under)))
          room_under.append(cadet)
    for room_upper in roomList[(48*i + 24):(48*i + 47)]:
      while len(room_upper) < 3:
        if len(upper) > 0:
          cadet = upper.pop(random_v(len(upper)))
          room_upper.append(cadet)
  return roomList

rooms = assignRoom(theCorps, companies, rooms)

def findRoom(cadet, roomList):
  for r in roomList:
    if cadet in r:
      return r

#print(findRoom(companies[0][0], rooms))
#tstcdt = companies[0][0]
#print(type(findRoom(tstcdt,rooms)))


#each inf cadet has 5% chance to infect another cadet in company and 3%that cadet is traced
#each inf cadet has 15% chance to infect another cadet on team and 7% that cadet is traced
#need way to do class schedules
def closeContacts(infCadet, q, compList, roomList, teamList, numInf):
    contacts = set()
    infCompany = findCompany(infCadet, compList)
    infRoom = findRoom(infCadet, roomList)
    infTeam = findTeam(infCadet, teamList)
    if infRoom == None or infTeam == None:
      return list(contacts)
    for cadet in infRoom:
      newInfection(cadet)
      numInf += 1
      q.append([cadet,0])
      contacts.add(cadet)
    for cdt in infCompany:
      infect = random_v(100)
      if infect <= 5:
        newInfection(cdt)
        numInf += 1
      trace = random_v(100)
      if trace <= 3:
          contacts.add(cdt)
    if not infTeam:
      for cdt in infTeam:
        infect = random_v(100)
        if infect <= 15:
          newInfection(cdt)
          numInf += 1
        trace1 = random_v(100)
        if trace1 <= 7:
          contacts.add(cdt)
    return list(contacts)

testPopulation = theCorps

beenTested = []

infectedPopulation = set()

quarantine = []

#isolation = []

numTested = 0
numInf = 0
numInfMonth = 0
numTP = 0
numTN = 0
numFP = 0
numFN = 0

#week and day counters
w = 1
d = 1
runs = 1
################################################################################
#Simulation
################################################################################
#while runs <= 100:

start = timeit.default_timer()
#Initial 100% testing
for cdt in theCorps:
  testResults = test(cdt)
  if testResults == "tP"or testResults == "fP" :
      quarantine.append([cdt,0])
      testPopulation.remove(cdt)

print("Quarantine Initial Length = {}".format(len(quarantine)))


while w <=16:
  print("Start week {}".format(w))

#weekly sentinel testing
  print("Test Population = {} at start of week {}".format(len(testPopulation), w)) #should have 16
  print(len(theCorps) -len(testPopulation) - len(beenTested) == 0)

#Creating weekly testing population
  sentinelCadets = []
  while len(sentinelCadets) < 108:
    testableCadet = random.choice(testPopulation)
    sentinelCadets.append(testableCadet)
    testPopulation.remove(testableCadet)
    numTested += 1
  print("cummulative number tested = {}, by week {}".format(numTested, w))
  print("sentinel testing count = {}".format(len(sentinelCadets)))

#Testing Sentinel population
  for cadet in sentinelCadets:
    testResults = test(cadet)
    if testResults == "tP":
      print(testResults)
      numTP += 1
      quarantine.append([cadet,0])
      testPopulation.remove(cadet)
      ccInf = closeContacts(cadet, quarantine, companies, rooms, teams, numInf)
      print(len(ccInf))
    elif testResults == "fP":
      print(testResults)
      numFP += 1
      quarantine.append([cadet,0])
      testPopulation.remove(cadet)
      ccInf = closeContacts(cadet, quarantine, companies, rooms, teams, numInf)
      print(len(ccInf))
    elif testResults == "fN":
      numFN += 1
    elif testResults == "tN":
      numTN += 1
  print("Contract tracing complete")

  while len(ccInf) > 0:
    for cdt in ccInf:
      if cdt not in testPopulation:
        pass
      else:
        testResults = test(cdt)
      if testResults == "tP":
        print(testResults)
        numTP += 1
        quarantine.append([cdt,0])
        testPopulation.remove(cdt)
        ccInf = closeContacts(cdt, quarantine, companies, rooms, teams, numInf)
        print(len(ccInf))
      elif testResults == "fP":
        print(testResults)
        numFP += 1
        quarantine.append([cdt,0])
        if cdt in testPopulation:
          testPopulation.remove(cdt)
          ccInf = closeContacts(cdt, quarantine, companies, rooms, teams, numInf)
          print(len(ccInf))
      elif testResults == "fN":
        numFN += 1
      elif testResults == "tN":
        numTN += 1
  print("2nd Set Contract tracing complete")


#Daily update of infection time/ quarantine population/ interaction infections
  while d <= 7:
    for cadet in theCorps:
      if cadet.infTime >= 1:
        cadet.infTime += 1
      if cadet.infTime >= 14:
        disinfection(cadet)
      for i in range(len(quarantine)):
        quarantine[i] = [quarantine[i], 0]
        quarantine[i][1] += 1
        if quarantine[i][1] >= 14:
          quaran
          freed = quarantine.pop(i)[0]
          if freed not in beenTested:
            testPopulation.append(freed)
      d += 1
    print("week {} and updates complete".format(w))


  if w == 4 or w == 8 or w == 12 or w == 16:
    numInfMonth += numInf
    numInf == 0
  d = 0
  w +=1
  print("Week {}".format(w))

end = timeit.default_timer()

print("Total number infected = {}".format(numInf))
print("Total number tested = {}".format(numTested))
print("TP: {} TN: {} FP: {}, FN: {}".format(numTN, numTP, numFP, numFN))
print("Total number in quarantine = {}".format(len(quarantine)))
print("Run Time: {}".format(end-start))

#  runs +=1


















