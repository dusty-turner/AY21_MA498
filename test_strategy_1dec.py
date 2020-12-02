#Author: Madison Teague
#Last Updated: 1 DEC


import random
import numpy as np
import math

#class CovidStatus(object):

#    def __init__(self, immune, infTime, symp, activeInf):
#        self.immune = immune #attribute for immunity classification (0/1)
#        self.infTime = infTime #attribute for infection time
#        self.symp = symp #attribute for symptomatic state classification (0/1)
#        self.activeInf = activeInf #attribute for active infection classification (0/1)

class Cadet(CovidStatus):

    def __init__(self, year, company, room, team, schedule, immune, infTime, symp, activeInf):
        self.year = year #class year 1 for cow/firstie, 0 for plebe/yuk
        self.company = company #company = "d2" etc.
        self.room = room #room written as string "e4023"
        self.team = team #all team names must be in camelCase and should include mens/womens if necessary,cadet is not on sport, sport = "none"
        self.schedule = schedule #List of courses written like "ma498_h24" (don't use day code use section code)
        self.immune = immune #attribute for immunity classification (0/1)
        self.infTime = infTime #attribute for infection time
        self.symp = symp #attribute for symptomatic state classification (0/1)
        self.activeInf = activeInf #attribute for active infection classification (0/1)

##function to create Bernoulli random variable
def bern():
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
def test(cadet, TP, TN, FP, FN):
  if cadet.activeInf == 1:
    results = random.randrange(0,100,10)
    if results >= .2:
      TP += 1
    else:
      FN += 1
    return("positive")
  else: 
    results = random.randrange(0,100,1)
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

##function to define close contacts
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

##Base lists of cadet attributes
companies = ["a1","b1","c1","d1","e1","f1","g1","h1","i1","a2","b2","c2","d2",
"e2","f2","g2","h2","i2","a3","b3","c3","d3","e3","f3","g3","h3","i3","a4","b4",
"c4","d4","e4","f4","g4","h4","i4"]

rooms = ["e1001","e1002","e1003","e1004","e1005","e1006","e1007","e1008","e1009",
"e1010","e1011","e1012","e1013","e1014","e1015","e1016","e1017","e1018","e1019",
"e1020","e1021","e1022","e1023","e1024","e1025","e1026","e1027","e1028","e1029",
"e1030","e1031","e1032","e1033","e1034","e1035","e1036","e2001","e2002","e2003",
"e2004","e2005","e2006","e2007","e2008","e2009","e2010","e2011","e2012","e2013",
"e2014","e2015","e2016","e2017","e2018","e2019","e2020","e2021","e2022","e2023",
"e2024","e2025","e2026","e2027","e2028","e2029","e2030","e2031","e2032","e2033",
"e2034","e2035","e2036", "e2037","e2038","e2039","e2040","e2041","e2042","e2043",
"e2044","e2045","e2046","e2047","e2048","e2048","e2049","e2050","e2051","e2052",
"e3001","e3002","e3003","e3004","e3005","e3006","e3007","e3008","e3009","e3010",
"e3011","e3012","e3013","e3014","e3015","e3016","e3017","e3018","e3019","e3020",
"e3021","e3022","e3023","e3024","e3025","e3026","e3027","e3028","e3029","e3030",
"e3031","e3032","e3033","e3034","e3035","e3036","e3037","e3038","e3039","e3040",
"e3041","e3042","e3043","e3044","e3045","e3046","e3047","e3048","e3048","e3049",
"e3050","e3051","e3052","e3053","3054","e4001","e4002","e4003","e4004","e4005",
"e4006","e4007","e4008","e4009","e4010","e4011","e4012","e4013","e4014","e4015",
"e4016","e4017","e4018","e4019","e4020","e4021","e4022","e4023","e4024","e4025",
"e4026","e4027","e4028","e4029","e4030","e4031","e4032","e4033","e4034","e4035",
"e4036","e4037","e4038","e4039","e4040","e4041","e4042","e4043","e4044","e4045",
"e4046","e4047","e4048","e4048","e4049","e4050","e5001","e5002","e5003","e5004",
"e5005","e5006","e5007","e5008","e5009","e5010","e5011","e5012","e5013","e5014",
"e5015","e5016","e5017","e5018","e5019","e5020","e5021","e5022","e5023","e5024",
"e5025","e5026","e5027","e5028","e5029","e5030","e5031","e5032","e5033","e5034",
"e5035","e5036","e5037","e5038","e5039","e5040","e5041","e5042","e5043","e5044",
"e5045","e5046","e5047","e5048","e5048","e5049","e5050","e5051","e5052","e6001",
"e6002","e6003","e6004","e6005","e6006","e6007","e6008","e6009","e6010","e6011",
"e6012","e6013","e6014","e6015","e6016","e6017","e6018","e6019","e6020","e6021",
"e6022","e6023","e6024","e6025","e6026","e6027","e6028","e6029","e6030","e6031",
"e6032","e6033","e6034","e6035","e6036","e6037","e6038","e6039","e6040","e6041",
"e6042","e6043","e6044","e6045","e6046","e6047","e6048","e6048","e6049","e6050",
"e6051","e6052","e6053","e6054","p1001","p1002","p1003","p1004","p1005","p1006",
"p1007","p1008","p1009","p1010","p1011","p1012","p1013","p1014","p1015","p1016",
"p1017","p1018","p1019","p1020","p1021","p1022","p1023","p1024","p1025","p1026",
"p1027","p1028","p1029","p1030","p2001","p2002","p2003","p2004","p2005","p2006",
"p2007","p2008","p2009","p2010","p2011","p2012","p2013","p2014","p2015","p2016",
"p2017","p2018","p2019","p2020","p2021","p2022","p2023","p2024","p2025","p2026",
"p2027","p2028","p2029","p2030","p2031","p3001","p3002","p3003","p3004","p3005",
"p3006","p3007","p3008","p3009","p3010","p3011","p3012","p3013","p3014","p3015",
"p3016","p3017","p3018","p3019","p3020","p3021","p3022","p3023","p3024","p3025",
"p3026","p3027","p3028","p3029","p3030","p3031","p3032","p3033","p3034","p3035",
"p3036","p3037","p3038","p3039","p4001","p4002","p4003","p4004","p4005","p4006",
"p4007","p4008","p4009","p4010","p4011","p4012","p4013","p4014","p4015","p4016",
"p4017","p4018","p4019","p4020","p4021","p4022","p4023","p4024","p4025","p4026",
"p4027","p4028","p4029","p4030","p4031","p4032","s1001","s1002","s1003","s1004",
"s1005","s1006","s1007","s1008","s1009","s1010","s1011","s1012","s1013","s1014",
"s1015","s1016","s2001","s2002","s2003","s2004","s2005","s2006","s2007","s2008",
"s2009","s2010","s2011","s2012","s2013","s2014","s2015","s2016","s2017","s2018",
"s2019","s2020","s2021","s2022","s2023","s2024","s2025","s2026","s2027","s2028",
"s2029","s2030","s2031","s2032","s2033","s2034" ]


teams = ["none","football", "track", "mLacrosse", "wLacrosse","mSoccer", "wSoccer",
"mSwim", "wSwim","volleyball", "wrestling", "hockey", "golf", "gymnastics",
"mBasketBall", "wBasketBall", "baseball", "softball", "mRugby", "wRugby", "mTennis",
"wTennis", "sprint", "mXC", "wXC", "rabs", "rifle", "strength"]
upperCourses = ["lw403_a1", "mx400_h8", "em481_i5", "ma381_e4"]
underCourses = ["lw403_a2", "mx400_h3", "em481_i7", "ma381_e23"]

covid1 = CovidStatus(0,0,0,0) #totally vulnerable
covid2 = CovidStatus(0,1,0,1) #actively infected, asymptomatic, one day of infection
covid3 = CovidStatus(1,0,0,0) #immune b/c already had disease
covid4 = CovidStatus(0,1,1,1) #activley infected, symptomatic, 1 day of infection

covidTypes = [covid1, covid2, covid3, covid4]

##base cadets to build corps from:
baseUpperCadet = Cadet(1, random.choice(companies), random.choice(rooms), 
random.choice(teams), [random.choice(upperCourses),random.choice(upperCourses),
random.choice(upperCourses),random.choice(upperCourses),random.choice(upperCourses),
random.choice(upperCourses)], random.choice([1,0]), 
random.choice([1,0]), random.choice([1,0]), random.choice([1,0]))

baseUnderCadet = Cadet(2, random.choice(companies), random.choice(rooms), 
random.choice(teams), [random.choice(underCourses),random.choice(underCourses),
random.choice(underCourses),random.choice(underCourses),random.choice(underCourses),
random.choice(underCourses)], random.choice([1,0]), 
random.choice([1,0]), random.choice([1,0]), random.choice([1,0]))

corps = [baseUpperCadet,baseUnderCadet]*2000

quarantine = []
isolation = []
numInf = 0
numTP = 0
numTN = 0
numFP = 0
numFN = 0

covid1 = covidStatus(0,0,0,0) #totally vulnerable
covid2 = covidStatus(0,1,0,1) #actively infected, asymptomatic, one day of infection
covid3 = covidStatus(1,0,0,0) #immune b/c already had disease
covid4 = covidStatus(0,1,1,1) #activley infected, symptomatic, 1 day of infection


#inital 100% test of corps?
#some kind of while loop for whole simulation?

w = 0

d = 0
while w <=16:
#function that randomly gives people coVID? 

#how many people infected per week?
  sentinel_cadets = [random.choice(corps)]*108

  for cadet in sentinel_cadets:
    testResults = test(cadet, numTP, numTN, numFP, numFN)
    if testResults == "positive" :
      numInf +=1
      quarantine.append(cadet)
      ccInf = closeContacts(cadet, corps)
#'randomly' infect cadts within close contacts (mainly roomates and DPE related people)
    for cdt in ccInf:
      if bern() == 1:
        newInfection(cdt)
      results = test(cdt, numTP, numTN, numFP, numFN)
      if results == 1:
        numInf +=1
        quarantine.add(cdt)
      elif cdt.room == cadet.room:
        quarantine.append(cdt)
  
  while d <= 7:
    for cadet in quarantine:
      cadet.infTime += 1
    d += 1
    
  if cadet.infTime == 14:
    disinfection(cadet)

  w +=1
  
  
  
print("Total number infected = {}".format(numInf))
print("TP: {} TN: {} FP: {}, FN: {}".format(numTN, numTP, numFP, numFN))

