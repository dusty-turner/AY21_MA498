####################################################
# Author: Madison Teague
# Translation of work done by COL Paul Evangelista
# Last updated 2 SEP 2020
####################################################
import random

#bernoulli random variable function
def bern():
  p = 1/2
  rn = random()
  rv = 0
  if (rn < p):
    rv = 1
  return rv

test = bern()
print(test)

#Function to create new infection; populates @infected, assigns infection time,
#assigns symptomatic condition (0 or 1)
