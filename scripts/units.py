import numpy as np
import math

# Constants

AU = 1.49e13
G  = 6.67408e-8
Msun  = 1.99e33

#  Input 

M            = Msun    # Stellar mass
r0           = 100*AU  # Reference radius
aspect_ratio = 0.1     # H/r (in code units this is equal to cs0)
alpha_SS     = 1e-2    #Shakura-Sunyaev alpha viscosity parameter

# Calculate units

unit_length   = r0
g0            = G*M
Omega         = np.sqrt(g0)*r0**(-1.5)   #Keplerian angular frequency
unit_time     = 1./Omega
unit_velocity = unit_length/unit_time

print "Units" 
print "Omega", Omega
print 'unit_length=',unit_length,' cm'
print 'unit_time=',unit_time,' s'
print 'unit_velocity=',unit_velocity,' cm/s'

number_density_carbon = 100
hydrogen_to_carbon_ratio = 1e4
number_density = hydrogen_to_carbon_ratio * number_density_carbon

atomic_mass_unit = 1.66054e-24
mean_molecular_weight  = 2.5
unit_density = number_density * mean_molecular_weight  * atomic_mass_unit

print 'unit_density=',unit_density,' g/cm3' 
print " " 

H = aspect_ratio * r0   # pressure scale height
cs = Omega * H 
gamma = 1
k = 1.380648e-16

T = cs**2 * (mean_molecular_weight  * atomic_mass_unit)/gamma/k

print "Thermal quantities"
print "Scale height H=", H/AU," AU"
print "Sound Speed, [m/s]=", cs/1e2
print "Temperature [K]=", T 
print " " 

#  Molecular viscosity 

sigma_coll = 2e-15 #cm2
mean_free_path = 1/(sigma_coll * number_density)

print "Microphysics" 
print "Mean free path=", mean_free_path/1e5," km"

nu_coll = np.sqrt(2/math.pi) * cs / (sigma_coll*number_density)

print "Molecular Viscosity (nu_coll) = ",nu_coll," cm2/s"
print " " 


# Turbulent viscosity

nu_turb = alpha_SS * cs * H 

print "Turbulent parameters" 
print "Turbulent Viscosity (nu_turb) = ",nu_turb," cm2/s"

#
#  Reynolds number of the largest scales of the flow
#
Re = nu_turb / nu_coll

V_L = np.sqrt(alpha_SS)*cs 
t_L = 1/Omega 

v_eta = Re**(-1/4)*V_L 
t_eta = Re**(-1/2) *t_L 

print "Reynolds number of largest eddies, Re=",Re

#
# Kolmogorov scaling
#

print "Velocity of largest eddies", V_L        ," cm/s"
print "Turnover time of largest eddies" , t_L  ," s"   

print "Velocity of smalles eddies", v_eta        ," cm/s"
print "Turnover time of smalles eddies" , t_eta  ," s"   
