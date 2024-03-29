# Generating-Coupled-Distribution

## coupled_dist.py file:
Generating 4-D Coupled Gaussian Distribution

This python script generates a 4-D coupled gaussian distribution. With coupled functions:

$\beta_{xI}$, $\beta_{xII},\beta_{yI},\beta_{yII}$ the 4 coupled beta functions.

$\alpha_{xI},\alpha_{xII},\alpha_{yI},\alpha_{yII}$ the 4 alpha functions; $\alpha = -\frac{1}{2}\beta'$. 

$u$ the coupling strength parameter, $\nu_{I,II}$ the phases of coupling in modes $I$ and $II$.

$\epsilon_{I,II}$ the eigen mode emittances for modes $I$ and $II$.

Based on the parametrization from Lebedev-Bogatz

## eigenparameters.py file:

Once the distribution is created, if a file is generated with it, eigenparameters.py file can calculate the eigen mode parameters:

It calculates: $\epsilon_{I,II}$ and $\epsilon_{x,y}$ from distribution.

