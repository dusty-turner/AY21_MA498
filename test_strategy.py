####################################################
# Author: Madison Teague
# Translation of work done by COL Paul Evangelista
# Last updated 2 SEP 2020
####################################################
import random
##maybe use object oriented programing?

class company:
    def __init__(self, co, room)
        self.co = co
        self.room = room
        
    def companyID(self):
        return f"Cadet is a member of {self.co} company."
    
    def roomID(self):
        return f"Cadet lives in room {self.room}."
    
    #Working function to randomly assign # of roomates
    #may not be useful b/c can just assign random rooms w/ max of 4 cadets
### def roomates(self):
###     rroomate = random.randrange(1,4,1) ##not actually distributed like this
###     return rroomat
    
    
class team:
    def __init__(self,sport):
        self.sport = sport
        
    def teamID(self):
        return f"Cadet is on {self.self}."
        
class schedule:
    def __init__(self, classes, section): #make classes and section a dictionary
        self.classes = classes
        self.sections = section
    
    def scheduleID(self):
        return f"Cadet is taking {self.classes} classes."

class cadet(company, team, schedule):
    
    def __init__(self, immune, infTime, symp, activeInf):
        self.immune = immune #attribute for immunity classification (0/1)
        self.infTime = infTime #attribute for infection time
        self.symp = symp #attribute for symptomatic state classification (0/1)
        self.activeInf = activeInf #attribute for active infection classification (0/1)

##function to create Bernoulli random variable
def bern():
    rv = random.randrange(0,2,1)
    return rv
    
#function to create new infection, assigns symptomatic condition (0 or 1)
def newInfection(cadet):
    if(cadet.immune == 1 || cadet.infTime != 0):
        pass
    else:
        cadet.symp = bern()
        cadet.activeInf = 1
#need somethig here for positive infections/total infections/infection time

#function to define close contacts
def closeContacts(infCadet, corps):
    contacts = []
    for cadet in corps:
        if (cadet.company == infCadet.company):
            if (cadet.room == infCadet.room):
                contacts += cadet
        if (cadet.team == infCadet.team):
            contacts += cadet
        for clas in infCadet.classes:
            if (cadet.class == clas && )##re-write for dictionary (key::value)
                contacts += cadet
                
    return contacts
        
