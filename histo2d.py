#!/usr/bin/env python

#Usage: histo2d.py file [nbin1 nbin2]
import sys

try:
    nbin1=int(sys.argv[2])
    nbin2=int(sys.argv[3])
except:
    nbin1=nbin2=100

x=[float(s.split()[0]) for s in open(sys.argv[1]).readlines()]
y=[float(s.split()[1]) for s in open(sys.argv[1]).readlines()]
minx=min(x)
miny=min(y)
dx=(max(x)-minx)*1.0001/nbin1
dy=(max(y)-miny)*1.0001/nbin2
bin=[[0]*nbin2 for i in range(nbin1)]
for (xx,yy) in zip(x,y):
    i=int((xx-minx)/dx)
    j=int((yy-miny)/dy)
    bin[i][j]+=1

#print bin

for i in range(nbin1):
    for j in range(nbin2):
        print minx+(i+0.5)*dx, miny+(j+0.5)*dy, bin[i][j]
    print





