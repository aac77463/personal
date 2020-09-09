import pencil as pc
import matplotlib.pyplot as plt 
import numpy as np
from pylab import *
from mpl_toolkits.axes_grid1 import make_axes_locatable
import sys

#tells you which orbit to import
ivar=100

# planet no PEH
#f1=pc.read_var(trimall=True,datadir='pehplanet/data',ivar=ivar)
# PHE no planet
#f2=pc.read_var(trimall=True,datadir='pehnoplanet/data',ivar=ivar)
# Both in
#f3=pc.read_var(trimall=True,datadir='nopehplanet/data',ivar=ivar)

#plt.imshow(ff.x,ff.y,ff.rho)

rad = np.linspace(0.4,2.5,256)#f1.x
theta = np.linspace(-pi,pi,256)#f1.y
rad2d,theta2d = np.meshgrid(rad,theta)

x2d = rad2d*np.cos(theta2d)
y2d = rad2d*np.sin(theta2d)

# Cartesian plot

fig, ((ax1, ax2, ax3)) = plt.subplots(1, 3,figsize=(18,5))

#fig = plt.figure()

ncolors=256
epsi = 1e-2 

f1rhopmax= 10. #np.log10(np.amax(f1.rhop))
f2rhopmax= 10. #np.log10(np.amax(f2.rhop))
f3rhopmax= 10. #np.log10(np.amax(f3.rhop))

maxval=4
minval=1

print 'max min of plots=', maxval, minval

#1st figure
ax1.set_aspect('equal')
tmp1 =  np.log10(theta2d**2 + 1. ) #f1.rhop[0,:,:]+epsi)
img1 = ax1.contourf(x2d, y2d, tmp1, np.linspace(minval, maxval, 256), vmin=0, vmax=4) #ncolors, vmin=minval, vmax=maxval) #X,Y & data2D must
ax1.set_title('no PEI planet')
#ax1.plot(np.cos(f1.t), np.sin(f1.t), 'ro')
orbit1 = plt.Circle((0,0), 1, color='red', alpha=0.5, fill=False)
ax1.add_artist(orbit1)
#divider = make_axes_locatable(ax1)
#cax1 = divider.append_axes("top", size = "5%", pad = 0.55)
##plt.colorbar(img1, cax=cax1, orientation="horizontal", ticks=[0,2,4])

#2nd figure
ax2.set_aspect('equal')
tmp2 = np.log10(theta2d**2 + 1. ) #f1.rhop[0,:,:]+epsi)f2.rhop[0,:,:]+epsi)
img2 = ax2.contourf(x2d, y2d, tmp2, np.linspace(minval, maxval, 256),vmin=0, vmax=4) #ncolors, vmin=minval, vmax=maxval) #X,Y & data2D must
ax2.set_title('PEI no planet')
#divider = make_axes_locatable(ax2)
#cax2 = divider.append_axes("top", size = "5%", pad = 0.55)
##plt.colorbar(img2, cax=cax2, orientation="horizontal", ticks=[0,2,4])

#3rd figure
ax3.set_aspect('equal')
tmp3 = np.log10(theta2d**2 + 1. ) #f1.rhop[0,:,:]+epsi)f3.rhop[0,:,:]+epsi)
img3 = ax3.contourf(x2d, y2d, tmp3, np.linspace(minval, maxval, 256), vmin=0, vmax=4) #ncolors, vmin=minval, vmax=maxval) #X,Y & data2D must
ax3.set_title('PEI and planet') 
#ax3.plot(np.cos(f3.t), np.sin(f3.t), 'ro')
orbit2 = plt.Circle((0,0), 1, color='red', alpha=0.5, fill=False)
ax3.add_artist(orbit2)
#divider = make_axes_locatable(ax3)
#cax3 = divider.append_axes("top", size = "5%", pad = 0.55)
##plt.colorbar(img3, cax=cax3, orientation="horizontal", ticks=[0,2,4])

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.01, 0.7])
fig.colorbar(img3, cax=cbar_ax)

#fig.colorbar(fig, orientation="horizontal", vmin=0, vmax=4)

plt.show()
