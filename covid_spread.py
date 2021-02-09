#COVID-19 Spread Through the Corps of Cadets
#Author: Madison Teague
#Last Updated: 31 January 2021

import random
import numpy as np
import math
import timeit

class Cadet():
  
  def __init__(self, year, immune, infTime, symp, knownInf):
    self.year = year #1 = cow/firstie, 2 = yuk/plebe
#    self.schedule = schedule 
    self.immune = immune #attribute for immunity classification (0/1)
    self.infTime = infTime #attribute for known infection time (0-14)
    self.symp = symp #attribute for symptomatic state classification (0/1)
    self.knownInf = knownInf #attribute for when infection is identified(0/1)
    
    
################################################################################
##base cadets to build corps from:
################################################################################

slug = []
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
t7 = []
t8 = []
t9 = []
t10 = []
t11 = []
t12 = []
t13 = []
t14 = []
t15 = []
t16 = []
t17 = []
t18 = []
t19 = []
t20 = []
t21 = []
t22 = []
t23 = []
t24 = []
t25 = []
t26 = []
t27 = []
t28 = []
t29 = []
t30 = []

teams = [slug, t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,
t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30]


upper1 = [Cadet(1,0,0,0,0)]*1600
upper2 = [Cadet(1,1,0,0,0)]*360
upper3 = [Cadet(1,1,1,0,0)]*35
upper4 = [Cadet(1,1,1,1,0)]*5

under1 = [Cadet(2,0,0,0,0)]*1600
under2 = [Cadet(2,1,0,0,0)]*360
under3 = [Cadet(2,1,1,0,0)]*35
under4 = [Cadet(2,1,1,1,0)]*5

type(upper1)

theCorps = upper1 + upper2 + upper3 + upper4 + under1 + under2 + under3 + under4

#function for random variables from uniform random distribution    
def random_v(x):
  rv = random.randrange(0,x,1)
  return(rv)

#random determination of symptoms
def sympRate():
  random_v(100)
  if rv >= 20:
    return(0)
  else: 
    return(1)
    
def weibull(k,lam):
  x = random.range(0,1000,1)
  rv = (k/lam)*(x/lam)**(k-1)*(math.exp((-x/lam)**k))
  return(rv)
  
#function to create new infections, assigns a symptomatic condition
def newInfection(cadet):
  if cadet.immune == 1 or cadet.infTime != 0:
    pass
  else:
    cadet.symp = sympRate()
    cadet.knownInf = 1
    cadet.infTime = 1
    
#TP rate = .8
#FN rate = .2
#TN rate = .99
#FP rate = .01

#Test function 
def test(cadet):
  if cadet.infTime >= 1:
    results = random_v(100)
    if results >= 20:
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

##Base lists of cadet attributes


def createCompanyList(top):
  i =   1
  finalList = []
  while i <= top:
    finalList.append([])
    i += 1
  return(finalList)  

companies = createCompanyList(36)


def assignCompany(corps, compList):
  for cadet in corps:
    comp = random.choice(compList)
    while len(comp) >= 120:
      comp = random.choice(compList)
    comp.append(cadet)
    
assignCompany(theCorps, companies)    

def findCompany(cadet, compList):
  for c in compList:
    if cadet in c:
#      print(type(c))
      return c


def assignTeam(corps, tmList):
  for cadet in corps:
    team = random.choice(tmList)
    if len(team) <= 50 and team != slug:
      team.append(cadet)
    elif team == slug and len(team) <= 2100:
      team.append(cadet)

assignTeam(theCorps, teams)

def findTeam(cadet, tmList):
  for t in tmList:
    if cadet in t:
      return t
  
def createRoomList(top):
  i =   1
  finalList = []
  while i <= top:
    finalList.append([])
    i += 1
  return(finalList)
  
rooms = createRoomList(1583)
  
def assignRoom(corps, compList, roomList):
  for cadet in corps:
    company = findCompany(cadet, compList)
    if cadet.year == 1:
      if compList.index(company) == 0:
        room = random.choice(roomList[0:21])
        while len(room) >= 3:
          room = random.choice(roomList[0:21])
        room.append(cadet)
      elif compList.index(company) == 1:
        room = random.choice(roomList[44:65])
        while len(room) >= 3:
          room = random.choice(roomList[44:65])
        room.append(cadet)
      elif compList.index(company) == 2:
        room = random.choice(roomList[88:109])
        while len(room) >= 3:
          room = random.choice(roomList[88:109])
        room.append(cadet)
      elif compList.index(company) == 3:
        room = random.choice(roomList[132:153])
        while len(room) >= 3:
          room = random.choice(roomList[132:153])
        room.append(cadet)    
      elif compList.index(company) == 4:
        room = random.choice(roomList[176:197])
        while len(room) >= 3:
          room = random.choice(roomList[176:197])
        room.append(cadet)
      elif compList.index(company) == 5:
        room = random.choice(roomList[220:241])
        while len(room) >= 3:
          room = random.choice(roomList[220:241])
        room.append(cadet)
      elif compList.index(company) == 6:
        room = random.choice(roomList[264:285])
        while len(room) >= 3:
          room = random.choice(roomList[264:285])
        room.append(cadet)
      elif compList.index(company) == 7:
        room = random.choice(roomList[308:329])
        while len(room) >= 3:
          room = random.choice(roomList[308:329])
        room.append(cadet)
      elif compList.index(company) == 8:
        room = random.choice(roomList[352:373])
        while len(room) >= 3:
          room = random.choice(roomList[352:373])
        room.append(cadet)
      elif compList.index(company) == 9:
        room = random.choice(roomList[396:417])
        while len(room) >= 3:
          room = random.choice(roomList[396:417])
        room.append(cadet)
      elif compList.index(company) == 10:
        room = random.choice(roomList[440:461])
        while len(room) >= 3:
          room = random.choice(roomList[440:461])
        room.append(cadet)
      elif compList.index(company) == 11:
        room = random.choice(roomList[484:505])
        while len(room) >= 3:
          room = random.choice(roomList[484:505])
        room.append(cadet)
      elif compList.index(company) == 12:
        room = random.choice(roomList[528:549])
        while len(room) >= 3:
          room = random.choice(roomList[528:549])
        room.append(cadet)
      elif compList.index(company) == 13:
        room = random.choice(roomList[572:593])
        while len(room) >= 3:
          room = random.choice(roomList[572:593])
        room.append(cadet)
      elif compList.index(company) == 14:
        room = random.choice(roomList[616:637])
        while len(room) >= 3:
          room = random.choice(roomList[616:637])
        room.append(cadet)
      elif compList.index(company) == 15:
        room = random.choice(roomList[660:681])
        while len(room) >= 3:
          room = random.choice(roomList[660:681])
        room.append(cadet)
      elif compList.index(company) == 16:
        room = random.choice(roomList[704:725])
        while len(room) >= 3:
          room = random.choice(roomList[704:725])
        room.append(cadet)    
      elif compList.index(company) == 17:
        room = random.choice(roomList[748:769])
        while len(room) >= 3:
          room = random.choice(roomList[748:769])
        room.append(cadet)
      elif compList.index(company) == 18:
        room = random.choice(roomList[792:813])
        while len(room) >= 3:
          room = random.choice(roomList[792:813])
        room.append(cadet)
      elif compList.index(company) == 19:
        room = random.choice(roomList[836:857])
        while len(room) >= 3:
          room = random.choice(roomList[836:857])
        room.append(cadet)
      elif compList.index(company) == 20:
        room = random.choice(roomList[880:901])
        while len(room) >= 3:
          room = random.choice(roomList[880:901])
        room.append(cadet)
      elif compList.index(company) == 21:
        room = random.choice(roomList[924:945])
        while len(room) >= 3:
          room = random.choice(roomList[924:945])
        room.append(cadet)
      elif compList.index(company) == 22:
        room = random.choice(roomList[966:989])
        while len(room) >= 3:
          room = random.choice(roomList[966:989])
        room.append(cadet)
      elif compList.index(company) == 23:
        room = random.choice(roomList[1012:1033])
        while len(room) >= 3:
          room = random.choice(roomList[1012:1033])
        room.append(cadet)
      elif compList.index(company) == 24:
        room = random.choice(roomList[1056:1077])
        while len(room) >= 3:
          room = random.choice(roomList[1056:1077])
        room.append(cadet)
      elif compList.index(company) == 25:
        room = random.choice(roomList[1100:1121])
        while len(room) >= 3:
          room = random.choice(roomList[1100:1121])
        room.append(cadet)    
      elif compList.index(company) == 26:
        room = random.choice(roomList[1144:1165])
        while len(room) >= 3:
          room = random.choice(roomList[1144:1165])
        room.append(cadet)    
      elif compList.index(company) == 27:
        room = random.choice(roomList[1188:1209])
        while len(room) >= 3:
          room = random.choice(roomList[1188:1209])
        room.append(cadet)
      elif compList.index(company) == 28:
        room = random.choice(roomList[1232:1253])
        while len(room) >= 3:
          room = random.choice(roomList[1232:1253])
        room.append(cadet)
      elif compList.index(company) == 29:
        room = random.choice(roomList[1276:1297])
        while len(room) >= 3:
          room = random.choice(roomList[1276:1297])
        room.append(cadet)
      elif compList.index(company) == 30:
        room = random.choice(roomList[1320:1341])
        while len(room) >= 3:
          room = random.choice(roomList[1320:1341])
        room.append(cadet)
      elif compList.index(company) == 31:
        room = random.choice(roomList[1364:1385])
        while len(room) >= 3:
          room = random.choice(roomList[1364:1385])
        room.append(cadet)
      elif compList.index(company) == 32:
        room = random.choice(roomList[1408:1429])
        while len(room) >= 3:
          room = random.choice(roomList[1408:1429])
        room.append(cadet)
      elif compList.index(company) == 33:
        room = random.choice(roomList[1452:1473])
        while len(room) >= 3:
          room = random.choice(roomList[1452:1473])
        room.append(cadet)
      elif compList.index(company) == 34:
        room = random.choice(roomList[1496:1517])
        while len(room) >= 3:
          room = random.choice(roomList[1496:1517])
        room.append(cadet)
      elif compList.index(company) == 35:
        room = random.choice(roomList[1541:1562])
        while len(room) >= 3:
          room = random.choice(roomList[1541:1562])
        room.append(cadet)
    if cadet.year == 2:
      if compList.index(company) == 0:
        room = random.choice(roomList[22:43])
        while len(room) >= 3:
          room = random.choice(roomList[22:43])
        room.append(cadet)
      elif compList.index(company) == 1:
        room = random.choice(roomList[66:87])
        while len(room) >= 3:
          room = random.choice(roomList[66:87])
        room.append(cadet)
      elif compList.index(company) == 2:
        room = random.choice(roomList[110:131])
        while len(room) >= 3:
          room = random.choice(roomList[110:131])
        room.append(cadet)
      elif compList.index(company) == 3:
        room = random.choice(roomList[154:175])
        while len(room) >= 3:
          room = random.choice(roomList[154:175])
        room.append(cadet)    
      elif compList.index(company) == 4:
        room = random.choice(roomList[198:219])
        while len(room) >= 3:
          room = random.choice(roomList[198:219])
        room.append(cadet)
      elif compList.index(company) == 5:
        room = random.choice(roomList[242:263])
        while len(room) >= 3:
          room = random.choice(roomList[242:263])
        room.append(cadet)
      elif compList.index(company) == 6:
        room = random.choice(roomList[286:307])
        while len(room) >= 3:
          room = random.choice(roomList[286:307])
        room.append(cadet)
      elif compList.index(company) == 7:
        room = random.choice(roomList[330:351])
        while len(room) >= 3:
          room = random.choice(roomList[330:351])
        room.append(cadet)
      elif compList.index(company) == 8:
        room = random.choice(roomList[374:395])
        while len(room) >= 3:
          room = random.choice(roomList[374:395])
        room.append(cadet)
      elif compList.index(company) == 9:
        room = random.choice(roomList[418:439])
        while len(room) >= 3:
          room = random.choice(roomList[418:439])
        room.append(cadet)
      elif compList.index(company) == 10:
        room = random.choice(roomList[462:483])
        while len(room) >= 3:
          room = random.choice(roomList[462:483])
        room.append(cadet)
      elif compList.index(company) == 11:
        room = random.choice(roomList[506:527])
        while len(room) >= 3:
          room = random.choice(roomList[506:527])
        room.append(cadet)
      elif compList.index(company) == 12:
        room = random.choice(roomList[550:571])
        while len(room) >= 3:
          room = random.choice(roomList[550:571])
        room.append(cadet)
      elif compList.index(company) == 13:
        room = random.choice(roomList[594:615])
        while len(room) >= 3:
          room = random.choice(roomList[594:615])
        room.append(cadet)
      elif compList.index(company) == 14:
        room = random.choice(roomList[638:659])
        while len(room) >= 3:
          room = random.choice(roomList[638:659])
        room.append(cadet)
      elif compList.index(company) == 15:
        room = random.choice(roomList[682:703])
        while len(room) >= 3:
          room = random.choice(roomList[682:703])
        room.append(cadet)
      elif compList.index(company) == 16:
        room = random.choice(roomList[724:747])
        while len(room) >= 3:
          room = random.choice(roomList[724:747])
        room.append(cadet)    
      elif compList.index(company) == 17:
        room = random.choice(roomList[770:791])
        while len(room) >= 3:
          room = random.choice(roomList[770:791])
        room.append(cadet)
      elif compList.index(company) == 18:
        room = random.choice(roomList[814:835])
        while len(room) >= 3:
          room = random.choice(roomList[814:835])
        room.append(cadet)
      elif compList.index(company) == 19:
        room = random.choice(roomList[858:879])
        while len(room) >= 3:
          room = random.choice(roomList[858:879])
        room.append(cadet)
      elif compList.index(company) == 20:
        room = random.choice(roomList[902:923])
        while len(room) >= 3:
          room = random.choice(roomList[902:923])
        room.append(cadet)
      elif compList.index(company) == 21:
        room = random.choice(roomList[946:967])
        while len(room) >= 3:
          room = random.choice(roomList[946:967])
        room.append(cadet)
      elif compList.index(company) == 22:
        room = random.choice(roomList[990:1011])
        while len(room) >= 3:
          room = random.choice(roomList[990:1011])
        room.append(cadet)
      elif compList.index(company) == 23:
        room = random.choice(roomList[1034:1055])
        while len(room) >= 3:
          room = random.choice(roomList[1034:1055])
        room.append(cadet)
      elif compList.index(company) == 24:
        room = random.choice(roomList[1078:1099])
        while len(room) >= 3:
          room = random.choice(roomList[1078:1099])
        room.append(cadet)
      elif compList.index(company) == 25:
        room = random.choice(roomList[1122:1143])
        while len(room) >= 3:
          room = random.choice(roomList[1122:1143])
        room.append(cadet)    
      elif compList.index(company) == 26:
        room = random.choice(roomList[1166:1187])
        while len(room) >= 3:
          room = random.choice(roomList[1166:1187])
        room.append(cadet)    
      elif compList.index(company) == 27:
        room = random.choice(roomList[1210:1231])
        while len(room) >= 3:
          room = random.choice(roomList[1210:1231])
        room.append(cadet)
      elif compList.index(company) == 28:
        room = random.choice(roomList[1254:1275])
        while len(room) >= 3:
          room = random.choice(roomList[1254:1275])
        room.append(cadet)
      elif compList.index(company) == 29:
        room = random.choice(roomList[1298:1319])
        while len(room) >= 3:
          room = random.choice(roomList[1298:1319])
        room.append(cadet)
      elif compList.index(company) == 30:
        room = random.choice(roomList[1342:1363])
        while len(room) >= 3:
          room = random.choice(roomList[1342:1363])
        room.append(cadet)
      elif compList.index(company) == 31:
        room = random.choice(roomList[1386:1407])
        while len(room) >= 3:
          room = random.choice(roomList[1386:1407])
        room.append(cadet)
      elif compList.index(company) == 32:
        room = random.choice(roomList[1430:1451])
        while len(room) >= 3:
          room = random.choice(roomList[1430:1451])
        room.append(cadet)
      elif compList.index(company) == 33:
        room = random.choice(roomList[1474:1495])
        while len(room) >= 3:
          room = random.choice(roomList[1474:1495])
        room.append(cadet)
      elif compList.index(company) == 34:
        room = random.choice(roomList[1518:1539])
        while len(room) >= 3:
          room = random.choice(roomList[1518:1539])
        room.append(cadet)
      elif compList.index(company) == 35:
        room = random.choice(roomList[1563:1584])
        while len(room) >= 3:
          room = random.choice(roomList[1563:1584])
        room.append(cadet)
        

#rooms = assignRoom(theCorps, companies, rooms)

def findRoom(cadet, roomList):
  for r in roomList:
    if cadet in r:
      print(type)
      return(r)

def closeContacts(infCadet, q, compList, roomList, teamList, numInf):
  #need way to do class schedules
    contacts = set()
    infCompany = findCompany(infCadet, compList)
    infRoom = findRoom(infCadet, roomList)
    print(type(infRoom))
    infTeam = findTeam(infCadet, teamList)
    for cadet in infRoom:
      newInfection(cadet)
      numInf += 1
      q.append(cadet)
      contacts.add(cadet)
    for cdt in infCompany:
      infect = random_v(100)
      if infect <= 10:
        newInfection(cdt)
        numInf += 1
        trace = random_v(100)
      if trace <= 3:
          contacts.add(cdt)
    if infTeam != slug:
      for cdt in infTeam:
        infect = random_v(100)
        if infect <= 15:
          newInfection(cdt)
          numInf += 1
        trace = random_v(100)
        if trace <= 7:
          contacts.add(cdt)
    return(contacts)
          
    
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
################################################################################
#Simulation
################################################################################
start = timeit.default_timer()   
    
#Initial 100% testing
for cdt in theCorps: 
  testResults = test(cdt)
  if testResults == "tP"or testResults == "fP" :
      quarantine.append([cdt,0])
      testPopulation.remove(cdt)

print("Quarantine Length = {}".format(len(quarantine)))    
 
      
while w <=16:
  
#weekly sentinel testing 
  print("Test Population = {}".format(len(testPopulation))) #should have 16

#Creating weekly testing population  
  sentinelCadets = []
  while len(sentinelCadets) <= 107:
    testableCadet = random.choice(testPopulation)
    sentinelCadets.append(testableCadet)
    testPopulation.remove(testableCadet)
    numTested += 1
  print("number tested = {}, week {}".format(numTested, w))
  print("number to test = {}".format(len(sentinelCadets)))
 
#Testing Sentinel population
  for cadet in sentinelCadets:
    testResults = test(cadet)
    if testResults == "tP":
      numTP += 1
      quarantine.append([cadet,0])
      testPopulation.remove(cadet)
      ccInf = closeContacts(cadet, quarantine, companies, rooms, teams, numInf)
    elif testResults == "fP":
      numFP += 1
      quarantine.append([cadet,0])
      testPopulation.remove(cadet)
      ccInf = closeContacts(cadet, quarantine, companies, rooms, teams, numInf)
    elif testResults == "fN":
      numFN += 1
    elif testResults == "tN":
      numTN += 1    
  print("Contract tracing complete")


#Daily update of infection time/ quarantine population/ interaction infections  
  while d <= 7:
    for cadet in theCorps:
      if cadet.activeInf == 1:
        cadet.infTime += 1
      if cadet.infTime >= 14:
        disinfection(cadet)
    for i in range(0,len(quarantine)):
      quarantine[i][1] += 1
      if quarantine[i][1] >= 14:
        freed = quarantine.pop(i)
        if freed not in beenTested:
          testPopulation.append(freed)
    d += 1
  
    
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

















    
    
