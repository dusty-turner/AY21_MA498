#COVID-19 Spread Through the Corps of Cadets
#Author: Madison Teague
#Last Updated: 23 April 2021

import random
#import numpy as np
#import math
import timeit

################################################################################
#Functions and cadet class
################################################################################

class Cadet(object):
  def __init__(self, year, immune, infTime, activeInf, symp, qTime, company, team, room, uniqueID):
    self.year = year #0 = cow/firstie, 1 = yuk/plebe
    self.immune = immune #attribute for immunity classification (0/1)
    self.infTime = infTime #attribute for known infection time (0-14)
    self.activeInf = activeInf #active infection marker (0/1)
    self.symp = symp #attribute for symptomatic state classification (0/1)
    self.qTime = qTime #attribute for time in quarantine (0-14)
    self.company = company #index of company in master company list
    self.team = team #index of tam in master team list
    self.room = room #index of room in master room list
    self.uniqueID = uniqueID #makes every cadet unique

#function for random variables from uniform random distribution
def random_v(x):
  rv = random.randrange(x)
  return rv

def yearID():
  rv = random_v(2)
  return rv

#15 % come back immune
def immuneID():
  rv = random_v(100)
  if rv >= 15:
    return 0
  else:
    return 1

def activeInfID():
  rv = random_v(100)
  if rv > 3:
    return 0
  else:
    return 1

#random determination of symptoms
def sympRate():
  rv = random_v(100)
  if rv >= 20:
    return 0
  else:
    return 1

#function to create new infections, assigns a symptomatic condition
def newInfection(cadet, infectList):
  if cadet.immune == 1 or cadet.activeInf == 1:
    pass
  else:
    infectList.append(cadet)
    cadet.activeInf = 1
    cadet.symp = sympRate()
    cadet.infTime = 1
#    return cadet, infectList

#Test function
def test(cadet):
  if cadet.activeInf == 1 and cadet.infTime >= 4:
    results = random_v(100)
    if results > 5:
      cadet.qTime = 1
      return("tP")
    else:
      return("fN")
  else:
    results = random_v(100)
    if results > 1:
       return ("tN")
    else:
      cadet.qTime = 1
      return("fP")

def disinfection(cadet, infectList):
    cadet.symp = 0
    cadet.immune = 1
    cadet.infTime = 0
    cadet.activeInf = 0
    cadet.qTime = 0
    if cadet in infectList:
      infectList.remove(cadet)
#    return cadet, infectList




################################################################################
#Building Simulation Environment
################################################################################

def makeGroup(i):
  compList = []
  for j in range(i):
    compList.append([j])
  return compList

def makeCorps(i):
  corps = []
  for j in range(i):
    cadet = Cadet(yearID(), immuneID(),0, activeInfID(), 0, 0, 0, 45, 0, j)
    if cadet.activeInf == 1:
      cadet.symp = sympRate()
    corps.append(cadet)
  return corps

def assignCompany(upper, under, compList):
  for c in compList:
    while len(c) < 62:
      cadet = random.choice(upper)
      c.append(cadet)
      cadet.company = c[0]
    while len(c) < 123:
      cadet = random.choice(under)
      c.append(cadet)
      cadet.company = c[0]
  return compList

def assignTeam(corps, tmList):
  for team in tmList:
    while len(team) < 37:
      cadet = random.choice(corps)
      team.append(cadet)
      cadet.team = team[0]
  return tmList

def assignRoom(upper, under, compList, roomList):
  for i in range(36):
    for room_under in roomList[(48*i):(48*i + 23)]:
      while len(room_under) < 3:
        cadet = random.choice(under[1:])
        room_under.append(cadet)
        cadet.room = room_under[0]
    for room_upper in roomList[(48*i + 24):(48*i + 47)]:
      while len(room_upper) < 3:
        cadet = random.choice(upper[1:])
        room_upper.append(cadet)
        cadet.room = room_upper[0]
  return roomList

def removeIndexes(list):
  for element in list:
    element.pop(0)


def closeContacts(infCadet, compList, roomList, teamList, infectList):
    contacts = []
    infCompany = compList[infCadet.company]
    infRoom = roomList[infCadet.room]
    if infCadet.team != 45:
      infTeam = teamList[infCadet.team]
    else:
      infTeam = []
    for cadet in infRoom:
      if cadet != infCadet:
        newInfection(cadet, infectList)
        contacts.append(cadet)
    for cdt in infCompany:
      if cdt != infCadet:
        infect = random_v(100)
        if infect < 10:
          newInfection(cdt, infectList)
          trace = random_v(100)
          if trace < 25:
            contacts.append(cdt)
    if not len(infTeam):
      pass
    else:
      for cdt in infTeam:
        if cdt != infCadet:
          infect = random_v(100)
          if infect < 15:
            newInfection(cdt, infectList)
            trace1 = random_v(100)
            if trace1 < 25:
              contacts.append(cdt)
    return contacts

companies = makeGroup(36)
teams = makeGroup(45)
rooms = makeGroup(1728)

#4392 cadets (122 per company)

theCorps = makeCorps(4392)
allunder = []
allupper = []

for cadet in theCorps:
  if cadet.year == 0:
    allupper.append(cadet)
  else:
    allunder.append(cadet)

companies = assignCompany(allupper, allunder, companies)
teams = assignTeam(theCorps, teams)
rooms = assignRoom(allupper, allunder, companies, rooms)

infected = []
numTested = 0
numTP = 0
numTN = 0
numFP = 0
numFN = 0
numQ = 0

removeIndexes(companies)
removeIndexes(teams)
removeIndexes(rooms)
#week and day counters
w = 1
d = 1
################################################################################
#Simulation
################################################################################
start = timeit.default_timer()


#Initial 100% testing
for cdt in theCorps:
  if cdt.activeInf == 1:
    infected.append(cdt)
  testResults = test(cdt)
  if testResults == "tP"or testResults == "fP" :
      cdt.qTime = 1

print("week, inf, co, team, result")
#print("week, numPos, numInf")
while w <=16:
#  print("Start week {}".format(w))

#Creating weekly testing population
  sentinelCadets = []
  while len(sentinelCadets) < 108:
    for i in range(36):
      testableCadet = random.choice(companies[i])
      if testableCadet.qTime == 0 and testableCadet not in sentinelCadets:
        sentinelCadets.append(testableCadet)


#Testing Sentinel population
  ccInf = []
  sentPos = 0
  for cadet in sentinelCadets:
    testResults = test(cadet)
    numTested += 1
    print("{},{},{},{},{},sentinel".format(w,cadet.activeInf, cadet.company, cadet.team, testResults))
    if testResults == "tP":
      numTP += 1
      sentPos += 1
      ccInf = ccInf + closeContacts(cadet, companies, rooms, teams, infected)
    elif testResults == "fP":
      numFP += 1
      sentPos += 1
      ccInf = ccInf + closeContacts(cadet, companies, rooms, teams, infected)
    elif testResults == "fN":
      numFN += 1
    elif testResults == "tN":
      numTN += 1
  #print("{}, {}, sentinel, {}".format(w,sentPos, len(infected)))

  contactPos = 0
  while len(ccInf) > 0:
    for cdt in ccInf:
      if cdt.qTime > 0:
        ccInf.remove(cdt)
      else:
        ccInf.remove(cdt)
        testResults = test(cdt)
        numTested += 1
        print("{},{},{},{},{},sentinelContact".format(w,cdt.activeInf, cdt.company, cdt.team, testResults))
        if testResults == "tP":
          numTP += 1
          contactPos += 1
        #  ccInf = ccInf + closeContacts(cdt, companies, rooms, teams, infected)
        elif testResults == "fP":
          numFP += 1
          contactPos += 1
        #  ccInf = ccInf + closeContacts(cdt, companies, rooms, teams, infected)
        elif testResults == "fN":
          numFN += 1
        elif testResults == "tN":
          numTN += 1
  #print("{}, {}, contact, {}".format(w,contactPos,len(infected)))

  #Daily update of infection time/ quarantine population/ interaction infections
  while d <= 7:
    for cadet in theCorps:
      if cadet.activeInf == 1:
        cadet.infTime += 1
        if cadet.infTime >= 14:
          disinfection(cadet, infected)
        elif cadet.infTime >= 4 and cadet.qTime == 0:
          for roomie in room[cadet.room]:
            newInfection(roomie, infected)
            ccInf = closeContacts(cadet, companies, rooms, teams, infected)
        elif cadet.symp == 1 and cadet.qTime == 0 and cadet.infTime >=5:
          testResults = test(cadet)
          numTested += 1
          print("{},{},{},{},{},symptomatic".format(w,cadet.activeInf, cadet.company, cadet.team, testResults))
          if testResults == "tP":
            numTP += 1
          elif testResults == "fP":
            numFP += 1
          elif testResults == "fN":
            numFN += 1
          elif testResults == "tN":
            numTN += 1
      if cadet.qTime >= 1:
        cadet.qTime += 1
        if cadet.qTime >= 14:
          cadet.qTime = 0
      d += 1

  print("week {} , {} infected in corps".format(w, len(infected)))

  d = 0
  w +=1

print("Total number tested = {}".format(numTested))
print("TP: {} TN: {} FP: {}, FN: {}".format(numTN, numTP, numFP, numFN))
for cdt in theCorps:
  if cdt.qTime > 0:
    numQ += 1
print("Total number in quarantine = {}".format(numQ))


end = timeit.default_timer()
print("Run Time: {}".format(end-start))


