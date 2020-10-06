#install.packages("CARBayesST")
#install.packages("CARBayes")
#install.packages("INLA", repos=c(getOption("repos"), INLA="https://inla.r-inla-download.org/R/stable"), dep=TRUE)

library("INLA")

#Simulated data in R
N = 100 #500, 5000, 25000, 100000  
x = rnorm(N, mean=6,sd=2)
y = rnorm(N, mean=x,sd=1) 
data = list(x=x,y=y,N=N)

#Inla Code
inla(y~x, family = c("gaussian"), data = data, control.predictor=list(link=1)) 
