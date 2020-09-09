import numpy as np
import pencil as pc
import math
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib

import matplotlib.pyplot as plt

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

f300=np.load('rhop_rho_300.npz')
f420=np.load('rhop_rho_300_420.npz')
nvar = 420

rho1=f300['rho'][0:300,:]
rhop1=f300['rhop'][0:300,:]
time1=np.arange(300) * 1.0

rho2=f420['rho']
rhop2=f420['rhop']
time2=f420['time']

rho  = np.concatenate((rho1,rho2))
rhop = np.concatenate((rhop1,rhop2))
time = np.concatenate((time1,time2))

dim=pc.read_dim()

fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10,10))

grid=pc.read_grid(trim=True)
rad = grid.x
phi = grid.y

ff=pc.read_var(trimall=True,ivar=nvar)

im1 = ax1.contourf(rad,time,rhop+1e-3,np.linspace(0.,4.,256),cmap='viridis')
divider = make_axes_locatable(ax1)
cax1 = divider.append_axes("top", size = "5%", pad = 0.55)
cb1 = plt.colorbar(im1,cax=cax1,orientation="horizontal",ticks=[0.,1.,2.,3.,4])
cb1.ax.set_title(r'$<\rho_d>/\rho_0$')
cb1.ax.xaxis.set_label_position('top')


im2 = ax2.contourf(rad,time,rho,np.linspace(rho.min(),rho.max(),256),cmap='inferno')
divider = make_axes_locatable(ax2)
cax2 = divider.append_axes("top", size = "5%", pad = 0.55)
cb2 = plt.colorbar(im2,cax=cax2,orientation="horizontal",ticks=[0.,0.25,0.5,0.75,1.0,1.25])
cb2.ax.set_title(r'$<\rho_g>/\rho_0$')
cb2.ax.xaxis.set_label_position('top')

r,p=np.meshgrid(rad,phi)

x = r*np.cos(p)
y = r*np.sin(p)

mm=np.log10(ff.rhop.max())
mlin = 1e-4

im3 = ax3.contourf(x,y,np.log10(ff.rhop+mlin),np.linspace(-4,mm,256),cmap='viridis')
divider = make_axes_locatable(ax3)
cax3 = divider.append_axes("top", size = "5%", pad = 0.55)
cb3 = plt.colorbar(im3,cax=cax3,orientation="horizontal",ticks=[-4,-3,-2,-1,0.,1.])
cb3.ax.set_title(r'$\log_{10} (\rho_d/\rho_0$)')
cb3.ax.xaxis.set_label_position('top')

im4 = ax4.contourf(x,y,ff.rho,np.linspace(ff.rho.min(),ff.rho.max(),256),cmap='inferno')
divider = make_axes_locatable(ax4)
cax4 = divider.append_axes("top", size = "5%", pad = 0.55)
cb4 = plt.colorbar(im4,cax=cax4,orientation="horizontal",ticks=[0, 0.25, 0.5,0.75,1.0,1.25,1.5])
cb4.ax.set_title(r'$\rho_g/\rho_0$')
cb4.ax.xaxis.set_label_position('top')

ax1.set_xlabel(r'$x/R_\odot$')
ax2.set_xlabel(r'$x/R_\odot$')
ax3.set_xlabel(r'$x/R_\odot$')
ax4.set_xlabel(r'$x/R_\odot$')

ax1.set_ylabel(r'$t/T_0$')
ax2.set_ylabel(r'$t/T_0$')
ax3.set_ylabel(r'$y/R_\odot$')
ax4.set_ylabel(r'$y/R_\odot$')

ax1.set_title("Dust density vs time")
ax2.set_title("Gas density vs time")
ax3.set_title("Dust density vs radius")
ax4.set_title("Gas density vs radius")

ax3.set_aspect("equal")
ax4.set_aspect("equal")

plt.tight_layout()
#plt.show()
plt.savefig("densities_vs_time.png")
