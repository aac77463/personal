import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pencil as pc
import math

#amount of orbits to be read
nvar=20
#reads dimensions of the data
dim=pc.read_dim()
#init a blank array for incoming data by resolution in x,y & orbit number
data_anim=np.zeros([dim.nx,dim.ny,nvar])

#small number to fix logarithmic error
epsi=1e-6

#init plot
fig, ax = plt.subplots()

#creates a blank array of the plots
ims = []

for ivar in range(nvar):
    #reads in data for each var
    ff = pc.read_var(trimall=True,ivar=ivar)
    #adds data from the rhop(dust) into the init. blank array
    data_anim[:,:,ivar] = ff.rhop + epsi
    #find the radial and phi directions
    rad, theta=ff.x, ff.y
    #add previous directions into a grid
    rad2d, theta2d = np.meshgrid(rad,theta)
    #creates ?????
    x2d = rad2d*np.cos(theta2d)
    y2d = rad2d*np.sin(theta2d)
    #creates the plot of the image for each iteration
    fmap=ax.contourf(x2d, y2d, np.log10(data_anim[:,:,ivar]), np.linspace(0,1e10,256))
    #for fcontour we have to use collections to loop
    add_arts=fmap.collections
    #appends each image to the new array
    ims.append(add_arts)

interval=20
fps=24
dpi=60
    
ani = animation.ArtistAnimation(fig,ims)
FFwriter=animation.FFMpegWriter()
ani.save('arelitest.mp4', writer = FFwriter)


