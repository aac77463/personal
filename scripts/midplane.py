
import pencil as pc
import matplotlib.pyplot as plt 
import numpy as np
from pylab import *
from mpl_toolkits.axes_grid1 import make_axes_locatable
import sys

dim=pc.read_dim()
par=pc.read_param()
ff=pc.read_var(trimall=True,ivar=40,magic=['tt','vort'])
#ff=pc.read_var(trimall=True,ivar=41,magic=['tt','vort'])
f0=pc.read_var(trimall=True,ivar=0 ,magic=['tt','vort'])

#rho0 =  1./ff.x^par.density_power_law
#lnrho0_midplane = -par.density_power_law * np.log(ff.x)
#tt0 = par.cs0^2/(par.cp*(par.gamma-1))
#tt0_midplane =  1./ff.x^par.temperature_power_law

#tmp_xy = np.exp(ff.lnrho[:,dim.ny/2,:]-f0.lnrho[:,dim.ny/2,:])
#
# Density
#
#rho_xy = np.zeros([dim.nz,dim.nx])
#for n in arange(dim.nz) : 
rho_xy = np.exp(ff.lnrho[:,dim.ny/2,:] - f0.lnrho[:,dim.ny/2,:])
#
# Temperature
#
#tt_xy = np.zeros([dim.nz,dim.nx])
#for n in arange(dim.nz) : 
tt_xy = ff.tt[:,dim.ny/2,:]/f0.tt[:,dim.ny/2,:]
print(np.min(tt_xy),np.max(tt_xy))
# 
# Vorticity
#
ooz  = zeros([dim.nz,dim.ny,dim.nx])
ooz0 = zeros([dim.nz,dim.ny,dim.nx])
phi = ff.y
sinth = np.sin(phi)
costh = np.cos(phi)
for m in range(dim.ny):
    ooz[:,m,:]  = -sinth[m]*ff.vort[1,:,m,:] + costh[m]*ff.vort[0,:,m,:]
    ooz0[:,m,:] = -sinth[m]*f0.vort[1,:,m,:] + costh[m]*f0.vort[0,:,m,:]

vort_xy = ooz[:,64,:]/ooz0[:,64,:]
print(np.min(vort_xy),np.max(vort_xy))

rad = ff.x*5.2
theta = ff.z
rad2d,theta2d = np.meshgrid(rad,theta)

x2d = rad2d*np.cos(theta2d)
y2d = rad2d*np.sin(theta2d)

#fig = plt.figure()
fig, ((ax1,ax2,ax3)) = plt.subplots(1,3,figsize=(12,5))
#ax = fig.add_subplot(111)


rho_xy_rotate = zeros([dim.nz,dim.nx])
tt_xy_rotate = zeros([dim.nz,dim.nx])
oo_xy_rotate = zeros([dim.nz,dim.nx])
for n in arange(dim.nz):
    norig = n + dim.nz/2
    if (norig >= dim.nz):
        norig = norig - dim.nz
    rho_xy_rotate[n,:] = rho_xy[norig,:]
    tt_xy_rotate[n,:] = tt_xy[norig,:]
    oo_xy_rotate[n,:] = vort_xy[norig,:]

ax1.set_aspect('equal')
im1 = ax1.contourf(x2d,y2d,rho_xy_rotate,np.linspace(0.,2.5,256))
ax1.set_xlim([-15,15])
ax1.set_ylim([-15,15])
ax1.set_ylabel("Y (AU)")
divider = make_axes_locatable(ax1)
cax1 = divider.append_axes("top", size = "5%", pad = 0.55)
plt.colorbar(im1,cax=cax1,orientation="horizontal",label=r'$\rho/\rho_0$',ticks=[0, 1, 2])

ax2.set_aspect('equal')
im2=ax2.contourf(x2d, y2d,tt_xy_rotate,np.linspace(0.8,2.2,256))
ax2.set_xlim([-15,15])
ax2.set_ylim([-15,15])
ax2.set_xlabel("X (AU)")
divider = make_axes_locatable(ax2)
cax2 = divider.append_axes("top", size = "5%", pad = 0.55)
plt.colorbar(im2,cax=cax2,orientation="horizontal",label=r'$T/T_0$',ticks=[1,1.5,2.])
for xlabel_i in ax2.axes.get_yticklabels():
    xlabel_i.set_fontsize(0.0)
    xlabel_i.set_visible(False)

ax3.set_aspect('equal')
im3=ax3.contourf(x2d, y2d, np.log10(oo_xy_rotate**2),np.linspace(-1.0,1.0,256))
ax3.set_xlim([-15,15])
ax3.set_ylim([-15,15])
divider = make_axes_locatable(ax3)
cax3 = divider.append_axes("top", size = "5%", pad = 0.55)
plt.colorbar(im3,cax=cax3,orientation="horizontal",label=r'$\log_{10}[(\omega/\omega_0)^2]$',ticks=[-1,0,1])
for xlabel_i in ax3.axes.get_yticklabels():
    xlabel_i.set_fontsize(0.0)
    xlabel_i.set_visible(False)

#plt.show()
plt.savefig('midplane_dens_tt_vort.png')

#contour,tmp_xy,x,y,/fill,/iso,lev=grange(0.,2.3,256)

