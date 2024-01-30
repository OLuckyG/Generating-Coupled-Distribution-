# Generating-Coupled-Distribution-
Generating 4-D Coupled Gaussian Distribution

This python script generates a 4-D coupled gaussian distribution. With coupled functions:

$\beta_{xI}$, $\beta_{xII},\beta_{yI},\beta_{yII}$ the 4 coupled beta functions.

$\alpha_{xI},\alpha_{xII},\alpha_{yI},\alpha_{yII}$ the 4 alpha functions; $\alpha = -\frac{1}{2}\beta'$. 

$u$ the coupling strength parameter, $\nu_{I,II}$ the phases of coupling in modes $I$ and $II$.

$\epsilon_{I,II}$ the eigen mode emittances for modes $I$ and $II$.

Based on the parametrization from Lebedev-Bogatz

$$
  \vec{z} = \frac{1}{2}\sqrt{\epsilon_{I}}\vec{v}_{I}e^{i\psi_{I}} + \frac{1}{2}\sqrt{\epsilon_{II}}\vec{v}_{II}e^{i\psi_{II}} + C.C
$$
Where, $C.C$ stands for complex conjugate
