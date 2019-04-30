import numpy as np
import matplotlib.pyplot as plt
import pencil as pc
from mpl_toolkits.axes_grid1 import make_axes_locatable

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)

epsi = 1e-3

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10,10))

dat=np.load('timeseries.npz')

x = dat.f.x
y = dat.f.y
rhop = dat.f.rhop
rho = dat.f.rho
rhop_av = dat.f.rhop_av
rho_av = dat.f.rho_av
t = dat.f.t
rad = dat.f.rad
theta = dat.f.theta

r,p=np.meshgrid(x,y)
x2d=r*np.cos(p)
y2d=r*np.sin(p)

rhoplog=np.log10(rhop+epsi)
rhoplog_av=np.log10(rhop_av+epsi)
print 'logrhop', np.amax(rhoplog)
print 'logrhop_av', np.amax(rhoplog_av)
print 'rho', np.amax(rho), np.amin(rho)
print 'rho_av', np.amax(rho_av), np.amin(rho_av)
mm1 = 2.3
mm2 = 1.7

im1 = ax1.contourf(x,t,np.log10(rhop_av+epsi),np.linspace(mm1-3,mm1,256),cmap='inferno')
ax1.set_axis_bgcolor('black')
divider = make_axes_locatable(ax1)
cax1 = divider.append_axes("top", size = "5%", pad = 0.55)
cb1 = plt.colorbar(im1,cax=cax1,orientation="horizontal",ticks=[-0.7,0.3,1.3,2.3])
cb1.ax.set_title(r'$\log_{10} (<\rho_d>/\rho_0)$')
cb1.ax.xaxis.set_label_position('top')
print 'plotting 1 of 4'

im2 = ax2.contourf(x,t,rho_av,np.linspace(0,4,256),cmap='viridis')
divider = make_axes_locatable(ax2)
cax2 = divider.append_axes("top", size = "5%", pad = 0.55)
cb2 = plt.colorbar(im2,cax=cax2,orientation="horizontal",ticks=[0,2,4])
cb2.ax.set_title(r'$<\rho_g>/\rho_0$')
cb2.ax.xaxis.set_label_position('top')
print 'plotting 2 of 4'

im3 = ax3.contourf(x2d,y2d,np.log10(rhop+epsi),np.linspace(mm2-3,mm2,256),cmap='inferno')
ax3.set_axis_bgcolor('black')
divider = make_axes_locatable(ax3)
cax3 = divider.append_axes("top", size = "5%", pad = 0.55)
cb3 = plt.colorbar(im3,cax=cax3,orientation="horizontal",ticks=[-1.3,-0.3,0.7,1.7])
cb3.ax.set_title(r'$\log_{10} (\rho_d/\rho_0$)')
cb3.ax.xaxis.set_label_position('top')
print 'plotting 3 of 4'

im4 = ax4.contourf(x2d,y2d,rho,np.linspace(0,5.5,256),cmap='viridis')
ax4.set_axis_bgcolor('black')
divider = make_axes_locatable(ax4)
cax4 = divider.append_axes("top", size = "5%", pad = 0.55)
cb4 = plt.colorbar(im4,cax=cax4,orientation="horizontal",ticks=[0,2.8,5.5])
cb4.ax.set_title(r'$\rho_g/\rho_0$')
cb4.ax.xaxis.set_label_position('top')
print 'plotting 4 of 4'


#img1=ax.contourf(x, t, np.log10(rhop+epsi), np.linspace(mm-5,mm,256))
 
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
plt.show()

#plt.gcf()#

#plt.savefig('densities_time_heating',dpi=600,bbox_inches='tight', format='pdf')

#print 'saved file'
