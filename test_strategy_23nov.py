#Author: Madison Teague
#Last Updated: 16 NOV


import random
import numpy as np
import math

 class covidStatus:

    def __init__(self, immune, infTime, symp, activeInf):
        self.immune = immune #attribute for immunity classification (0/1)
        self.infTime = infTime #attribute for infection time
        self.symp = symp #attribute for symptomatic state classification (0/1)
        self.activeInf = activeInf #attribute for active infection classification (0/1)

class cadet:

    def __init__(self, year, company, room, team, schedule, covidStatus):
        self.year = year #class year 1 for cow/firstie, 0 for plebe/yuk
        self.company = company #company = "d2" etc.
        self.room = room #room written as string "e4023"
        self.team = team #all team names must be in camelCase and should include mens/womens if necessary,cadet is not on sport, sport = "none"
        self.schedule = schedule #List of courses written like "ma498_h24" (don't use day code use section code)

    def companyID(self):
        return(f"Cadet is a member of {self.company} company.")

    def roomID(self):
        return(f"Cadet lives in room {self.room}.")

    def teamID(self):
        return(f"Cadet is on {self.self}.")

    def scheduleID(self):
        return(f"Cadet is taking {self.courses}.")

    def cadetArray(self):
      cadetList = list(self.year, self.company, self.room, self.schedule, self.covidStatus)
      cadetArr = np.array(cadetList)
      return(cadetArr)


##function to create Bernoulli random variable
def bern(x,y):
    rv = random.randrange(0,2,1)
    return(rv)
    
def weibull(k,lam):
  x = random.range(0,1000,1)
  rv = (k/lam)*(x/lam)**(k-1)*(math.exp((-x/lam)**k))
  return(rv)

#function to create new infection, assigns symptomatic condition (0 or 1)
def newInfection(cadet):
    if(cadet.immune == 1 or cadet.infTime != 0):
        pass
    else:
        cadet.symp = bern()
        cadet.activeInf = 1
        cadet.infTime = 1
#need somethig here for positive infections/total infections/infection time


#need new distribution (weibull?)
#TP rate = .8
#FN rate = .2
#TN rate = .99
#FP rate = .01

#need way to come up with TP/TN/FP/FN generation
def test(cadet):
  if cadet.activeInf == 1:
    results = random.randrange(0,1,.1)
    if results >= .2:
      TP += 1
    else:
      FN += 1
    return("positive")
  else: 
    results = random.randrange(0,1,.01)
    if results >= .01:
      TN += 1
    else:
      FP += 1
  return("negative")   

def disinfection(cadet):
    cadet.symp = 0
    cadet.activeInf = 0
    cadet.immune = 1
    cadet.infTime = 0

#function to define close contacts
#returns set of close contacts for a cadet
#defines close cadets as roomates, teammates, and class sections
def closeContacts(infCadet, corps):
  #need way to mark teams/sections/companies as infected
    contacts = set()
    for cadet in corps:
        if cadet == infCadet:
            pass
        if (cadet.company == infCadet.company):
            if (cadet.room == infCadet.room):
                contacts.add(cadet)
        if (cadet.team == infCadet.team):
            contacts.add(cadet)
        if (cadet.year == infCadet.year):
          for course in infCadet.schedule:
              if course in cadet.schedule:
                  contacts.add(cadet)
    return(contacts)
 
  

################################################################################
#simulation
################################################################################

#Initial Parameters?
#corps = [cadet1,cadet2]*1000
#corpsArr = np.array(corps)
companies = ["a1","b1","c1","d1","e1","f1","g1","h1","i1","a2","b2","c2","d2",
"e2","f2","g2","h2","i2","a3","b3","c3","d3","e3","f3","g3","h3","i3","a4","b4",
"c4","d4","e4","f4","g4","h4","i4"]
quarantine = []
Isolation = []
numInf = 0
numTP = 0
numTN = 0
numFP = 0
numFN = 0

covid1 = covidStatus(0,0,0,0) #totally vulnerable
covid2 = covidStatus(0,1,0,1) #actively infected, asymptomatic, one day of infection
covid3 = covidStatus(1,0,0,0) #immune b/c already had disease
covid4 = covidStatus(0,4,1,1) #activley infected, symptomatic, 4 days of infection

#some kind of while loop for whole simulation?
n = 0

#inital 100% test of corps?

while n<=16:

#function that randomly gives people coVID. 
#how many people infected per week?
  
  sentinel_cadets = random.choice(corps, k=108)

  for cadet in sentinel_cadets:
    test_results = test(cadet)
    if test(cadet) == "positive" :
      numInf +=1
      quarantine.append(cadet)
      ccInf = closeContacts(cadet, corps)
#'randomly' infect cadts within close contacts (mainly roomates and DPE related people)
    for cdt in ccInf:
      if bern() == 1:
        newInfection(cdt)
      results = test(cdt)
      if results == 1:
        numInf +=1
        quarantine.add(cdt)
      elif cdt.room = cadet.room:
        quarantine.append(cdt)
  

      
  for cadet in quarantine:
    cadet.infTime += 7
    
    if cadet.infTime == 14:
      disinfection(cadet)

#need to follow when to take cadet out of quarantine
  n+=1
