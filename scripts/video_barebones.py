
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pencil as pc
import math

def run(n):
    data=np.random.rand(10,10)
    fmap = plt.contourf(data,16)
    print n,' of ',nframes,' done'        
    return fmap

######

nframes = 100
interval = 10
fps=24
dpi=100

fig = plt.figure()

# orbit

ani = animation.FuncAnimation(fig, run, nframes, interval=interval) #blit=True, repeat=False,init_func=init)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=fps, metadata=dict(artist='Me'))
ani.save('test.mp4',writer=writer,dpi=dpi)
#plt.show()
