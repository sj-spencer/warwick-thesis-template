#!/usr/bin/env python
# coding=UTF-8

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.style as style
style.use('classic')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('figure', autolayout=True)

fig,ax = plt.subplots(figsize=(5.5,3.5))

x = np.linspace(0,270e-6)

coeff1 = (1.05e-1,1.81e2,2.02e5,6.47e8)
coeff2 = (5.28,3.16e2,6.60e5,1.80e8)
dens351 = coeff1[0] + coeff1[1]*x + coeff1[2]*x**2 + coeff1[3]*x**3
temp351 = coeff2[0] + coeff2[1]*x + coeff2[2]*x**2 + coeff2[3]*x**3

ax.plot(x/1e-6,dens351*10,label=r'$n_e \times 10$ (351nm)',color='blue',ls='-')
ax.plot(x/1e-6,temp351,label=r'$T_e$ (351nm)',color='green',ls='-')

coeff3 = (8.21e-2,1.52e2,2.46e5,3.55e8)
coeff4 = (3.85,9.50e2,1.42e6,-1.27e9)
dens248 = coeff3[0] + coeff3[1]*x + coeff3[2]*x**2 + coeff3[3]*x**3
temp248 = coeff4[0] + coeff4[1]*x + coeff4[2]*x**2 + coeff4[3]*x**3

ax.plot(x/1e-6,dens248*10,label=r'$n_e \times 10$ (248nm)',color='blue',ls='--')
ax.plot(x/1e-6,temp248,label=r'$T_e$ (248nm)',color='green',ls='--')

coeff5 = (7.06e-2,1.66e2,3.95e4,1.01e9)
coeff6 = (3.01,1.47e3,1.31e6,-2.27e9)
dens193 = coeff5[0] + coeff5[1]*x + coeff5[2]*x**2 + coeff5[3]*x**3
temp193 = coeff6[0] + coeff6[1]*x + coeff6[2]*x**2 + coeff6[3]*x**3

ax.plot(x/1e-6,dens193*10,label=r'$n_e \times 10$ (193nm)',color='blue',ls='dashdot') 
ax.plot(x/1e-6,temp193,label=r'$T_e$ (193nm)',color='green',ls='dashdot')

ax.set_xlim(left=0,right=270)
#ax.legend(loc='best')
ax.grid(color='black',alpha=0.4)
ax.set_xlabel('$x$ $[\mu m]$')
ax.set_title(r'd) $n_e\times 10$ and $T_e$ profiles for 351(-), 248($-$$-$), and 193(-.) nm.',loc='left')

plt.show()
