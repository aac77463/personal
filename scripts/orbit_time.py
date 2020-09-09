import numpy as np

AU = 1.49e13
G = 6.67408e-8
Msun = 1.99e33

masses = [1.75,2.02,1.28,1.8,2.9,1]
radii_unadj = [86,100,24,60,110,200]
masses = np.array(masses)
radii_unadj = np.array(radii_unadj)

radii_adj = radii_unadj/2.

m_solar = Msun*masses

g0 = np.zeros([5])
Omega = np.zeros([5])
orbtime = np.zeros([5])

for i in masses:
    g0 = G*masses[i]
    print g0
    Omega[i] = np.sqrt(g0)*radii_adj[i]**(-3./2)
    print Omega
    orbtime = 1./Omega
    print orbtime

#print 'omega', Omega
#print 'time', orbtime, 's'

norm = orbtime/60/60/24/365
print norm
