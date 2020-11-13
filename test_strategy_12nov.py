#Author: Madison Teague
#Last Updated: 12 NOV


import random
import numpy as np

    
    
    #Working function to randomly assign # of roomates
    #may not be useful b/c can just assign random rooms w/ max of 4 cadets
### def roomates(self):
###     rroomate = random.randrange(1,4,1) ##not actually distributed like this
###     return rroomate
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
def bern():
    rv = random.randrange(0,2,1)
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
#need way to come up with TP/TN/FP/FN generation
def test(cadet):
  if cadet.activeInf == 1:
    results = bern()
  else: 
    results = bern()
  return(results)   

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
quarantine = []
softHold = []
numInf = 0
numTP = 0
numTN = 0
numFP = 0
numFN = 0

covid1 = covidStatus(0,0,0,0) #totally vulnerable
covid2 = covidStatus(0,1,0,1) #actively infected, asymptomatic, one day of infection
covid3 = covidStatus(1,0,0,0) #immune b/c already had disease
covid4 = covidStatus(0,4,1,1) #activley infected, symptomatic, 4 days of infection

newInfection(cadet1)

if test(cadet1) == 1:
  numInf +=1
  quarantine.add(cadet)
  
#need to follow when to take cadet out of quarantine


ccInf = closeContacts(cadet1, corpsArr)

#'randomly' infect cadts within close contacts (mainly roomates and DPE related people)
for cadet in ccInf:
  if bern() == 1:
    newInfection(cadet)
  results = test(cadet)
  if results == 1:
    numInf +=1
    quarantine.add(cadet)
  elif cadet.room = cadet1.room:
    quarantine.add(cadet)



