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

#x = [0.528,0.618,0.718,0.813,0.918,1.032,1.164]
#y2 = np.transpose([23.933,31.890,40.731,49.131,58.414,68.493,80.164])
#
#z=x[:,np.newaxis] * y[np.newaxis,:]
#
#xx, yy = np.meshgrid(x,y2)

epsi = 1e-3

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10,10))

dat=np.load('pnp_10-1.0_iso_200.npz')

x = dat.f.x
y = dat.f.y
rhop = dat.f.rhop
rho = dat.f.rho
rhop_av = dat.f.rhop_av
rho_av = dat.f.rho_av
t = dat.f.t/(2*np.pi)
rad = dat.f.rad
theta = np.linspace(-np.pi, np.pi*1.1, len(y))

r,p=np.meshgrid(x,y)
x2d=r*np.cos(p)
y2d=r*np.sin(p)

rhoplog=np.log10(rhop+epsi)
rhoplog_av=np.log10(rhop_av+epsi)
print 'logrhop', np.amax(rhoplog)
print 'logrhop_av', np.amax(rhoplog_av)
print 'rho', np.amax(rho), np.amin(rho)
print 'rho_av', np.amax(rho_av), np.amin(rho_av)
mm1 = 1
mm2 = 1.7

im1 = ax1.contourf(x,t,np.log10(rhop_av+epsi),np.linspace(mm1-3,mm1,256),cmap='inferno')
#ax1.contourf(xx,yy,z,'w')
ax1.set_axis_bgcolor('black')
divider = make_axes_locatable(ax1)
cax1 = divider.append_axes("top", size = "5%", pad = 0.55)
cb1 = plt.colorbar(im1,cax=cax1,orientation="horizontal",ticks=[-2,-1,0,1]) 
cb1.ax.set_title(r'$\log_{10}\left(\langle\rho_d\rangle/\rho_0\right)$')
cb1.ax.xaxis.set_label_position('top')
#adding a new line
norb=34# number of orbits
ax1.plot(x,x**1.5 * norb,color='black')
ax1.set_ylim([0,100])
#ax1.plot(x,x**2 * norb,color='black',linestyle='--')
print 'plotting 1 of 4'

im2 = ax2.contourf(x,t,rho_av,np.linspace(0,1.3,256),cmap='viridis')
divider = make_axes_locatable(ax2)
cax2 = divider.append_axes("top", size = "5%", pad = 0.55)
cb2 = plt.colorbar(im2,cax=cax2,orientation="horizontal",ticks=[0,0.65,1.3])
cb2.ax.set_title(r'$\langle\rho_g\rangle/\rho_0$')
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

im4 = ax4.contourf(x2d,y2d,rho,np.linspace(0,1.3,256),cmap='viridis')
ax4.set_axis_bgcolor('black')
divider = make_axes_locatable(ax4)
cax4 = divider.append_axes("top", size = "5%", pad = 0.55)
cb4 = plt.colorbar(im4,cax=cax4,orientation="horizontal",ticks=[0,0.65,1.3])
cb4.ax.set_title(r'$\rho_g/\rho_0$')
cb4.ax.xaxis.set_label_position('top')
print 'plotting 4 of 4'


#img1=ax.contourf(x, t, np.log10(rhop+epsi), np.linspace(mm-5,mm,256))
 
ax1.set_xlabel(r'$r/r_0$')
ax2.set_xlabel(r'$r/r_0$')
ax3.set_xlabel(r'$x/r_0$')
ax4.set_xlabel(r'$x/r_0$')

ax1.set_ylabel(r'$t/T_0$')
ax2.set_ylabel(r'$t/T_0$')
ax3.set_ylabel(r'$y/r_0$')
ax4.set_ylabel(r'$y/r_0$')

ax1.set_title("Dust density vs time")
ax2.set_title("Gas density vs time")
ax3.set_title("Dust density vs radius")
ax4.set_title("Gas density vs radius")

ax3.set_aspect("equal")
ax4.set_aspect("equal")

plt.tight_layout()
#plt.title('10 to 1, 100 orbits')
#plt.show()

#plt.gcf()#

plt.savefig('densities_heating_10to1_200.png',dpi=300)

print 'saved file'
