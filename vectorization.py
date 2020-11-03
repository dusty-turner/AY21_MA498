#Author: Madison Teague
#Last Updated: 29 September


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
        self.team = team #all team names must be in camelCase and should include m/w if necessary,cadet is not on sport, sport = "none"
        self.schedule = schedule # list of sections written like "ma498_h24" (don't use day code use section code)

    def companyID(self):
        return(f"Cadet is a member of {self.company} company.")

    def roomID(self):
        return(f"Cadet lives in room {self.room}.")

    def teamID(self):
        return(f"Cadet is on {self.team}.")

    def scheduleID(self):
        return(f"Cadet is taking {self.schedule}.")

class company:
  
  def __init__(self, cadetList):
    self.cadetList = cadetList #list (or array) containing all cadets in company.(name ID)
    
class room:
  def __init__(self, occupants):
    self.occupants = occupants #list (or array) containing all cadets in room.(name ID)
    
class team:
  
  def __init__(self, teamRoster):
    self.teamRoster = teamRoster #list (or array) containing all cadets on team.(name ID)
  
  
class section: 
  
  def __init__(self,students):
    self.students = students #list(or array) containing all cadets in section. (name ID)
    
    
def bern():
    rv = random.randrange(0,2,1)
    return(rv)

#function to create new infection, assigns symptomatic condition (0 or 1)
#function to create new infection, assigns symptomatic condition (0 or 1)
def newInfection(cadet):
    if(cadet.immune == 1 or cadet.infTime != 0):
        pass
    else:
        cadet.symp = bern()
        cadet.activeInf = 1
        cadet.infTime = 1
#need somethig here for positive infections/total infections/infection time

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
              if (course in cadet.schedule and cadet.schedule[course] == infCadet.schedule[course]):
                  contacts.add(cadet)
    return(contacts)

def groupInfect(infCadet, corps):
    team = infCadet.team
    infCadetArr = cadetArray(infCadet)
    if(team != "none"):
      for cdt in corps:
        cdtArr = cadetArray(cdt)
        teamRoster = np.where(cdtArr[3] == infCadetArr[3],cdt,)


def closeContacts2(infCadet, corps):
#need cadet to be array and corps to be array
    for cadet in corps:
      if(cadet == infCadet):
          pass
      cadetArr = cadetArray(cadet)
      infCadetArr = cadetArray(infCadet)
      for i in range(5):
        np.where(cadetArr[i] == infCadetArr[i],cadet)
#need something to return list of close contacts

def infect(contacts):
    for cadet in contacts:
      newInfection(cadet)


#testing what I got
courseDictX = {
    "lw403":"a12",
    "mx400":"h3",
    "em481":"i15",
    "ma381":"e27",
    "ma498":"j44",
    "se402":"i37"
}

courseDictY = {
    "mx400":"h3",
    "cy305":"j13",
    "ma381":"e27",
    "ss307":"g3",
    "em481":"i37"
}

courseDictZ = {
    "ma206":"a12",
    "ms200":"h3",
    "pe215":"i15",
    "ss202":"j27",
    "ev203":"j44",
    "py201":"i37"
}

covid1 = covidStatus(0,0,0,0) #totally vulnerable
covid2 = covidStatus(0,1,0,1) #actively infected, asymptomatic, one day of infection
covid3 = covidStatus(1,0,0,0) #immune b/c already had disease
covid4 = covidStatus(0,4,1,1) #activley infected, symptomatic, 4 days of infection

cadetX = cadet("1","d2", "e4023", "none", courseDictX, covid3)
cadetY = cadet("1", "d2", "e4031", "softball", courseDictY, covid4)
cadetZ = cadet("2", "e4", "s3015","softball",courseDictZ, covid1)

testCorps = [cadetX,cadetY,cadetZ]
closeTest = closeContacts(cadetY,testCorps)
type(closeTest)
print(closeTest)


#simulation parameters

quarantineCt = 0


#simulation functions
#need how to select a cadet to be tested
#need random assignment of test result
#need count for while in quarantine




