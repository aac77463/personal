
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pencil as pc
import math

def quantities_individual(x,y,vx,vy):
    rad  =  np.sqrt(x**2 + y**2)
    phi  =  np.arctan2(y,x)
    vrad =  np.cos(phi)*vx + np.sin(phi)*vy
    vphi = -np.sin(phi)*vx + np.cos(phi)*vy
    
    return rad,phi,vrad,vphi

def quantities_pair(x1,y1,vx1,vy1,x2,y2,vx2,vy2):
    x=x1-x2
    y=y1-y2
    vx=vx1-vx2
    vy=vy1-vy2
    
    rad  =  np.sqrt(x**2 + y**2)
    v2   =  vx**2 + vy**2
    sma  =  1./(2./rad - v2)
    phi  =  np.arctan2(y,x)
    vr   =  np.cos(phi)*vx + np.sin(phi)*vy
    vphi = -np.sin(phi)*vx + np.cos(phi)*vy
    Lphi =  vphi * rad
    ecc  =  np.sqrt(1 - Lphi**2/sma)
    
    return rad,vr,vphi,Lphi,sma,ecc

def get_orbit(r,phi,a,ecc):
    #r and phi are instantaneous position;
    #calculate true anomaly from position
    f = np.arccos(1/ecc * ((a/r) * (1-ecc**2) - 1))
    #calculate argument of periastron
    omega = phi-f
    #a,e, and argument of periastron given; calculate full orbit
    rorb = a*(1-ecc**2)/(1+ecc*np.cos(tht-omega))
    #output x and y of orbit
    xorb = rorb*np.cos(tht)
    yorb = rorb*np.sin(tht)
    
    return xorb,yorb

def data_gen(i):
    x1_orb,y1_orb = get_orbit(r1[i],phi1[i],a1[i],ecc[i])
    x2_orb,y2_orb = get_orbit(r2[i],phi2[i],a2[i],ecc[i])

    xq1=ts.xq1[i] * unit_length
    yq1=ts.yq1[i] * unit_length
    xq2=ts.xq2[i] * unit_length
    yq2=ts.yq2[i] * unit_length
    x1_orb=x1_orb * unit_length
    y1_orb=y1_orb * unit_length
    x2_orb=x2_orb * unit_length
    y2_orb=y2_orb * unit_length
        
    return xq1,yq1,xq2,yq2,x1_orb,y1_orb,x2_orb,y2_orb

def init():
    ax.set_ylim(-0.6*unit_length, 0.6*unit_length)
    ax.set_xlim(-0.6*unit_length, 0.6*unit_length)
    del x1data[:]
    del y1data[:]
    del x2data[:]
    del y2data[:]
    del x3data[:]
    del y3data[:]
    del x4data[:]
    del y4data[:]
    del x5data[:]
    del y5data[:]
    del x6data[:]
    del y6data[:]
    line1.set_data(x1data, y1data)
    line2.set_data(x2data, y2data)
    orbit1.set_data(x3data, y3data)
    orbit2.set_data(x4data, y4data)
    dot1.set_data(x5data, y5data)
    dot2.set_data(x6data, y6data)
    
    return [line1,line2,orbit1,orbit2,dot1,dot2]

def run(n):
    # update the data
    x1,y1,x2,y2,x1orb,y1orb,x2orb,y2orb = data_gen(n)
    x1data.append(x1)
    y1data.append(y1)
    x2data.append(x2)
    y2data.append(y2)
    nx=len(x1data)
    ny=len(y1data)
        
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    if ( (max(x1orb) < xmax/2) and
         (min(x1orb) > xmin/2) and
         (max(y1orb) < ymax/2) and
         (min(y1orb) > ymin/2)):
        ax.set_xlim(xmin/2, xmax/2)
        ax.set_ylim(ymin/2, ymax/2)
        ax.figure.canvas.draw()

    ntail=max([int(10*xmax/unit_length-1),1])
#
# Little tail if visible
#    
    if (nx < ntail):
        line1.set_data(x1data, y1data)
        line2.set_data(x2data, y2data)
    else:
        line1.set_data(x1data[nx-ntail:nx-1], y1data[ny-ntail:ny-1])
        line2.set_data(x2data[nx-ntail:nx-1], y2data[ny-ntail:ny-1])
#
#  Orbit
#
    orbit1.set_data(x1orb,y1orb)
    orbit2.set_data(x2orb,y2orb)
#
#  Dot -- location of UT, and physical size
#
    x1dot,y1dot=[],[]
    x2dot,y2dot=[],[]
    tht=np.linspace(0,2*math.pi,10)
    for i in range(1,10):
        rad=0.0016*unit_length * i/10.
        x1dot.append(rad*np.cos(tht)+x1)
        y1dot.append(rad*np.sin(tht)+y1)

        x2dot.append(rad*np.cos(tht)+x2)
        y2dot.append(rad*np.sin(tht)+y2)

    dot1.set_data(x1dot,y1dot)
    dot2.set_data(x2dot,y2dot)

    print n,' of ',nframes,' done'
    title.set_text(r'$a$='+str(int(sma[n]*unit_length))+' km; $t$='+str(int(time[n]))+' yr')
        
    return [line1,line2,orbit1,orbit2,dot1,dot2]

######

ts=pc.read_ts()

#nframes=len(ts.t)

par=pc.read_param()
par2=pc.read_param(param2=True)
m2 = par.pmass[1]
m1 = 1-m2
tau=par2.stokesnumber[0]

tht=np.linspace(0.,2*math.pi,100)

unit_length = 6.27e3 #(km)
unit_time   = 250.   #(yr)

time = unit_time * ts.t/2/math.pi 

r1,phi1,vrad1,vphi1   = quantities_individual(ts.xq1,ts.yq1,ts.vxq1,ts.vyq1)
r2,phi2,vrad2,vphi2   = quantities_individual(ts.xq2,ts.yq2,ts.vxq2,ts.vyq2)
rad,vr,vphi,lphi,sma,ecc = quantities_pair   (ts.xq1,ts.yq1,ts.vxq1,ts.vyq1,
                                              ts.xq2,ts.yq2,ts.vxq2,ts.vyq2)

tmp = abs(rad-0.0016)
imin = np.argmin(tmp)
nframes = imin
interval = 10
movie_time_seconds = nframes*interval/1000. 
fps      = nframes/movie_time_seconds

print 'interval,movie_time_seconds,fps=',interval,movie_time_seconds,fps

# From Dermott & Murray
a1 = m2/(m1+m2) * sma
a2 = m1/(m1+m2) * sma
h1 = lphi*(m2/(m1+m2))**2
h2 = lphi*(m1/(m1+m2))**2

fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xlabel("x (km)")
ax.set_ylabel("y (km)")

#title = ax.text(0.5,0.95, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},transform=ax.transAxes, ha="center")
title = ax.text(0.5,0.95, "", transform=ax.transAxes)

#tht=np.linspace(0.,2*math.pi,100)
#ax.plot(0.5*np.cos(tht), 0.5*np.sin(tht),linewidth=0.5,linestyle=':',color='grey')

# orbit
orbit1, = ax.plot([], [],linewidth=0.5,linestyle=':',color='blue')
orbit2, = ax.plot([], [],linewidth=0.5,linestyle=':',color='red')

# tail
line1, = ax.plot([], [],linewidth=2,linestyle='--',color='blue')
line2, = ax.plot([], [],linewidth=2,linestyle='--',color='red')

# dot
dot1, = ax.plot([], [],color='blue')
dot2, = ax.plot([], [],color='red')

ax.grid()
x1data, y1data = [], []
x2data, y2data = [], []
x3data, y3data = [], []
x4data, y4data = [], []
x5data, y5data = [], []
x6data, y6data = [], []

ani = animation.FuncAnimation(fig, run, nframes, blit=True, interval=interval,repeat=False,init_func=init)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=fps, metadata=dict(artist='Me'))
ani.save('ut_st1e3_01rh.mp4',writer=writer,dpi=300)

#plt.show()
