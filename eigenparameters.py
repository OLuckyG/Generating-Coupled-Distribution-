## Created by OluckyG
import pandas as pd
import numpy as np

## Reading the file:
file = pd.read_csv("file.out",delim_whitespace=True).values ## Add skiprows= i for skipping rows if the csv file has more than 1 line of headers

## Depending on the file arrangement change the reading values:
## Assuming: xarray --> 0th column
##         : xparray --> 1st column
##         : yarray --> 2nd column
##         : yparray -> 3rd column

x = file[:,0]
xp = file[:,1]
y = file[:,2]
yp = file[:,3]

N = len(x) ## number of particles


## Creating parameters for calculating eigenmode emittances from distribution:
## The second moments:
sumxx = 0.0 
sumxxp = 0.0
sumxpxp = 0.0
sumyy = 0.0
sumyyp = 0.0
sumypyp = 0.0
sumxy = 0.0
sumxyp = 0.0
sumyxp = 0.0
sumxpyp = 0.0
meanx = np.mean(x)
meanxp = np.mean(xp)
meany = np.mean(y)
meanyp = np.mean(yp)
for i in range(N):
	sumxx += (x[i] - meanx)**2
	sumxxp += (x[i] - meanx)*(xp[i] - meanxp)
	sumxpxp += (xp[i] - meanxp)**2
	sumyy += (y[i] - meany)**2
	sumyyp += (y[i] - meany)*(yp[i] - meanyp)
	sumypyp += (yp[i] - meanyp)**2
	sumxy += (x[i] - meanx)*(y[i] - meany)
	sumxyp += (x[i] - meanx)*(yp[i] - meanyp)
	sumyxp += (y[i] - meany)*(xp[i] - meanxp)
	sumxpyp += (yp[i] - meanyp)*(xp[i] - meanxp)

sumxx = sumxx/N
sumxxp = sumxxp/N
sumxpxp = sumxpxp/N
sumyy = sumyy/N
sumyyp = sumyyp/N
sumypyp = sumypyp/N
sumxy = sumxy/N
sumxyp = sumxyp/N
sumyxp = sumyxp/N
sumxpyp = sumxpyp/N

## In order to find the RMS eigenmode emittances, we need to use 4x4 Sigma matrix and 4x4 symplectic unit matrix: S

S = np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]]) ## symplectic unit matrix

Sigmaarray = np.array([[sumxx,sumxxp,sumxy,sumxyp],[sumxxp,sumxpxp,sumyxp,sumxpyp],[sumxy,sumyxp,sumyy,sumyyp],[sumxyp,sumxpyp,sumyyp,sumypyp]]) ## 4x4 Sigma matrix

## epsilon_{4D} squared is the determinant of the Sigma matrix

emit4Dsq = np.linalg.det(Sigmaarray)
emit4D = np.sqrt(emit4Dsq)

## Applying the formula to find the eigen mode RMS emittances:
product = np.matmul(Sigmaarray,S)
squaredp = np.matmul(product,product)
trace = np.trace(squaredp)

emit1 = (1/2)*np.sqrt(-trace + np.sqrt((trace**2) - 16*emit4Dsq))
emit2 = (1/2)*np.sqrt(-trace - np.sqrt((trace**2) - 16*emit4Dsq))

## calculating epsx and epsy as well:

emitx = np.sqrt(sumxx*sumxpxp - sumxxp**2)
emity = np.sqrt(sumyy*sumypyp - sumyyp**2)


## Printing:

print("RMS epsilonI:",emit1)
print("RMS epsilonII:",emit2)
print("RMS epsilonx:",emitx)
print("RMS epsilony:",emity)





