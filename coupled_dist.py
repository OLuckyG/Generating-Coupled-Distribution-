## This script is created by OluckyG
import numpy as np
import random as random
from numpy import mean,sqrt
import matplotlib.pyplot as plt
## Coupling parameters
u = 0.5 ## coupling strength
nuI = np.pi/2   ## Phase of coupling mode I
nuII = np.pi/2  ## Phase of coupling mode II

## Coupled functions 
betaxI = 1.0
betaxII = 1.0
betayI = 1.0
betayII = 1.0
alfaxI = 0.0
alfaxII = 0.0
alfayI = 0.0
alfayII = 0.0

## eigen mode RMS emittances:
epsI = 1e-6
epsII = 1e-8

## Defining the coefficients
xImax = sqrt(epsI*betaxI)
xIImax = sqrt(epsII*betaxII)
yImax = sqrt(epsI*betayI)
yIImax = sqrt(epsII*betayII)
xIpcoef = sqrt(epsI/betaxI)
xIIpcoef = sqrt(epsII/betaxII)
yIpcoef = sqrt(epsI/betayI)
yIIpcoef = sqrt(epsII/betayII)

## Number of particles
Npart = 100000

## Arrays for normalized distribution:
xnormarray = [0]*Npart
xpnormarray = [0]*Npart
ynormarray = [0]*Npart
ypnormarray = [0]*Npart

## Main particle array:
xarray = [0]*Npart
xparray = [0]*Npart
yarray = [0]*Npart
yparray = [0]*Npart

## Loop for gaussian distribution
for i in range(Npart):
	xnormarray[i] = random.gauss(0,1.0)
	xpnormarray[i] = random.gauss(0,1.0)
	ynormarray[i] = random.gauss(0,1.0)
	ypnormarray[i] = random.gauss(0,1.0)

## Loop for the particle coordinates:
for i in range(Npart):
	xarray[i] = xImax*xnormarray[i] + xIImax*(ynormarray[i]*np.cos(nuII) - ypnormarray[i]*np.sin(nuII))
	xparray[i] = upxIcoef*(-alfaxI*xnormarray[i]+(1-u)*xpnormarray[i]) + upxIIcoef*(-alfaxII*(ynormarray[i]*np.cos(nuII) - ypnormarray[i]*np.sin(nuII)) + u*(ypnormarray[i]*np.cos(nuII)+ynormarray[i]*np.sin(nuII)))
	yarray[i] = yIImax*ynormarray[i] + yImax*(xnormarray[i]*np.cos(nuI) - xpnormarray[i]*np.sin(nuI))
	yparray[i] = upyIcoef*(-alfayI*(xnormarray[i]*np.cos(nuI) - xpnormarray[i]*np.sin(nuI)) + u*(xpnormarray[i]*np.cos(nuI) + xnormarray[i]*np.sin(nuI))) + upyIIcoef*(-alfayII*ynormarray[i] + (1-u)*ypnormarray[i])

## Creating 2D histograms:
## x-x'

plt.hist2d(xarray,xparray,bins=100,cmap=plt.cm.jet)
plt.colorbar()
plt.xlabel("x")
plt.ylabel("x'")
plt.title("x-x' phase space")
plt.show()
plt.clf()

## y-y'
plt.hist2d(yarray,yparray,bins=100,cmap=plt.cm.jet)
plt.xlabel("y")
plt.ylabel("y'")
plt.title("y-y' phase space")
plt.show()
plt.clf()

## x-y
plt.hist2d(xarray,yarray,bins=100,cmap=plt.cm.jet)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("x-y space")
plt.show()
plt.clf()
## x'-y
plt.hist2d(xparray,yarray,bins=100,cmap=plt.cm.jet)
plt.xlabel("x'")
plt.ylabel("y")
plt.title("x'-y phase space")
plt.show()
plt.clf()
## x-y'
plt.hist2d(xarray,yparray,bins=100,cmap=plt.cm.jet)
plt.xlabel("x")
plt.ylabel("y'")
plt.title("x-y' phase space")
plt.show()
plt.clf()
## x'-y'
plt.hist2d(xparray,yparray,bins=100,cmap=plt.cm.jet)
plt.xlabel("x'")
plt.ylabel("y'")
plt.title("x'-y' space")
plt.show()
plt.clf()


