import pencil as pc
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from mpl_toolkits.axes_grid1 import make_axes_locatable
import sys

plt.rcParams['image.cmap'] = 'inferno'
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['xtick.labelsize']=20
plt.rcParams['ytick.labelsize']=20

ivar=15

f1 = pc.read_var(trimall=True, ivar=ivar, datadir='../05_m3_10-0_pnp/')
f2 = pc.read_var(trimall=True, ivar=ivar, datadir='../05_pnp_1to1/')
f3 = pc.read_var(trimall=True, ivar=ivar, datadir='../05_pnp_2to1/')
f4 = pc.read_var(trimall=True, ivar=ivar, datadir='../05_pnp_5to1/')
f5 = pc.read_var(trimall=True, ivar=ivar, datadir='../05_pnp_10to1/')

rhop1 = f1.rhop
rhop2 = f2.rhop
rhop3 = f3.rhop
rhop4 = f4.rhop
rhop5 = f5.rhop


rad = f1.x
theta = f1.y
rad2d, theta2d = np.meshgrid(rad,theta)

x2d = rad2d*np.cos(theta2d)
y2d = rad2d*np.sin(theta2d)

#fig, ((ax1 ,ax2, ax3),(ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=(20,10), sharey=True, sharex=True)
#fig.subplots_adjust(hspace=0, wspace=0)


fig=plt.figure(figsize=(20,10))
ax1 = plt.subplot2grid((8,12), (0,0), colspan=4, rowspan=4)
ax2 = plt.subplot2grid((8,12), (4,0), colspan=4, rowspan=4)
ax3 = plt.subplot2grid((8,12), (2,4), colspan=4, rowspan=4)
ax4 = plt.subplot2grid((8,12), (0,8), colspan=4, rowspan=4)
ax5 = plt.subplot2grid((8,12), (4,8), colspan=4, rowspan=4)


titlesize=36
labelsize=36

epsi=1e-10

rhopmax1 = np.amax(f1.rhop)
rhopmax2 = np.amax(f2.rhop)
rhopmax3 = np.amax(f3.rhop)
rhopmax4 = np.amax(f4.rhop)
rhopmax5 = np.amax(f5.rhop)


mm1=np.log10(rhopmax1)
mm2=np.log10(rhopmax2)
mm3=np.log10(rhopmax3)
mm4=np.log10(rhopmax4)
mm5=np.log10(rhopmax5)

mm=1.7


print "rhopmax1", mm1
print "rhopmax2", mm2
print "rhopmax3", mm3
print "rhopmax4", mm4
print "rhopmax5", mm5
print f1.t

ax1.set_aspect('equal')
img1=ax1.contourf(x2d, y2d, np.log10(rhop1 + epsi), np.linspace(mm-4, mm, 256))
ax1.plot(np.cos(f1.t), np.sin(f1.t), 'wo', alpha=0.4)
orbit1 = plt.Circle((0,0), 1, color='white', alpha=0.4, fill=False)
ax1.add_artist(orbit1)
ax1.set_ylabel(r'PEI:1/2:1',fontsize=labelsize)
ax1.set_axis_bgcolor('black')

ax2.set_aspect('equal')
img2=ax2.contourf(x2d, y2d, np.log10(rhop2 + epsi), np.linspace(mm-4, mm, 256))
ax2.set_ylabel(r'PEI:1:1',fontsize=labelsize)
ax2.set_axis_bgcolor('black')

ax3.set_aspect('equal')
img3=ax3.contourf(x2d, y2d, np.log10(rhop3 + epsi), np.linspace(mm-4, mm, 256))
ax3.set_axis_bgcolor('black')
ax3.set_ylabel(r'PEI:1:2',fontsize=labelsize)

ax4.set_aspect('equal')
img4=ax4.contourf(x2d, y2d, np.log10(rhop4 + epsi), np.linspace(mm-4, mm, 256))
ax4.set_axis_bgcolor('black')
ax4.set_ylabel(r'PEI:1:5',fontsize=labelsize)

ax5.set_aspect('equal')
img5=ax5.contourf(x2d, y2d, np.log10(rhop5 + epsi), np.linspace(mm-4, mm, 256))
ax5.set_axis_bgcolor('black')
ax5.set_ylabel(r'PEI:1:10',fontsize=labelsize)


#Adding the labels of each run to the plot

props = dict(boxstyle='square', facecolor='white', alpha=1)

ax1.text(0.1, 0.95, 'F', transform=ax1.transAxes, fontsize=18, verticalalignment='top', horizontalalignment='right', bbox=props)
ax2.text(0.1, 0.95, 'G', transform=ax2.transAxes, fontsize=18, verticalalignment='top', horizontalalignment='right', bbox=props)
ax3.text(0.1, 0.95, 'H', transform=ax3.transAxes, fontsize=18, verticalalignment='top', horizontalalignment='right',bbox=props)
ax4.text(0.1, 0.95, 'I', transform=ax4.transAxes, fontsize=18, verticalalignment='top', horizontalalignment='right', bbox=props)
ax5.text(0.1, 0.95, 'J', transform=ax5.transAxes, fontsize=18, verticalalignment='top', horizontalalignment='right', bbox=props)


fig.subplots_adjust(right=0.8)
cbar_ax=fig.add_axes([0.81, 0.15, 0.01, 0.7])
cbar = plt.colorbar(img1, cax=cbar_ax, ticks=[-0.8,0,0.8,1.6,2.4,3.2])
cbar.ax.tick_params(labelsize=24)
cbar.set_label(r'$log_{10}(\Sigma_{d} / \Sigma_{d,0})$', size=40)

ax1.tick_params(colors='white')
ax2.tick_params(colors='white')
ax3.tick_params(colors='white')
ax4.tick_params(colors='white')
ax5.tick_params(colors='white')


labels = len(ax1.get_xticklabels())
for i in range(labels):
    ax1.get_yticklabels()[i].set_color('black')
    ax2.get_yticklabels()[i].set_color('black')
    ax2.get_xticklabels()[i].set_color('black')
    ax3.get_yticklabels()[i].set_color('black')
    ax3.get_xticklabels()[i].set_color('black')
    ax4.get_yticklabels()[i].set_color('black')
    ax4.get_xticklabels()[i].set_color('black')
    ax5.get_xticklabels()[i].set_color('black')
    ax5.get_yticklabels()[i].set_color('black')

plt.setp(ax1.get_xticklabels(),visible=False)
plt.setp(ax4.get_xticklabels(),visible=False)

plt.show()
#plt.savefig('../figs/05_10-0_dust_global.png', bbox_inches='tight')
#plt.savefig('.../home/areli/Desktop/05_10-0_dust_global.png', bbox_inches='tight')
