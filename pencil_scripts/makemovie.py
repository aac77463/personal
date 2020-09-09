from pylab import *
import sys
import os
import pencil as pc
from pencil.files.npfile import npfile
from pencil.files.dim import read_dim
from pencil.files.var import read_var

def make_movie(field='rhop', datadir='./', proc=-1, extension='xy',
               format='native', tmin=0., tmax=1.e38, transform='',
               oldfile=False):

    ff = pc.read_var(trimall=True)
    dim = pc.read_dim()
    
    rhop = ff.rhop
    r2d, phi2d = meshgrid(ff.x, ff.y)
    x = r2d*cos(phi2d).astype('float16')
    y = r2d*sin(phi2d).astype('float16')

    epsi = 1e-4
    hsize = dim.nx
    vsize = dim.ny
    dimz = int(dim.nz/2)
    
    lg_rhop_xy = log10(rhop[dimz,...] + epsi)
    max_rhop = lg_rhop_xy.max()
    
    datadir = os.path.expanduser(datadir)

    if proc < 0:
        filename = datadir + '/slice_' + field + '.' + extension
    else:
        filename = datadir + '/proc' + str(proc) + '/slice_' + field \
                   + '.' + extension

    dim = read_dim(datadir, proc)

    if dim.precision == 'D':
        precision = 'd'

    plane = zeros((vsize, hsize), dtype=precision)

    infile = npfile(filename, endian=format)
    files = []

    ifirst = True
    islice = 0

    fig = figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.set_facecolor('black')
    clbr = contourf(x, y, plane, linspace(max_rhop-4,max_rhop, 256))
    cbar = fig.colorbar(clbr)
    while True:
        try:
            raw_data = infile.fort_read(precision)
        except ValueError:
            break
        except TypeError:
            break

        #if oldfile:
         #   t = raw_data[-1]
          #  plane = raw_data[:-1].reshape(vsize, hsize)
        #else:
        #    t = raw_data[-2]
        #    plane = raw_data[:-2].reshape(vsize, hsize)
        t = raw_data[-2]
        plane = log10(raw_data[:-2].reshape(vsize, hsize))

        res = linspace(plane.max()-4, plane.max(), 256)
                    
        if transform:
            exec('plane = plane' + transform)

        if t > tmin and t < tmax:
            ax.set_facecolor('black')
            ax.set_aspect('equal')
            ax.cla()
            ax.contourf(x, y, plane, res)
#            ax.contourf(x, y, plane, linspace(max_rhop-4,max_rhop, 256))
            ax.set_title('Dust Density t=%s' % ('{:.2f}'.format(t)))
            fname = '_img%03d.png' % islice
            print('Saving frame' + fname)
            fig.savefig(fname, dpi=300)
            files.append(fname)

            if ifirst:
                print("----islice----------t")
            print("{0:10} {1:10.3e}".format(islice, t))

            ifirst = False
            islice += 1
            
    os.system("mencoder 'mf://_img*.png' -mf type=png:fps=24 -ovc lavc -lavcopts vcodec=wmv2 -oac copy -o animation.mpg")
    infile.close()

make_movie(field='rhop', datadir='data/', proc=-1, extension='xy',
           format='native', tmin=0., tmax=1.e8, transform='',
           oldfile=False)
