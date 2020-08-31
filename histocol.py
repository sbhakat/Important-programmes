#!/usr/bin/python2

#Usage: histocol.py file column [nbin [ start stop] ]
import sys

col=int(sys.argv[2])

y=[float(s.split()[col-1]) for s in open(sys.argv[1]).readlines() if s[0]!='#' ]

try:
    nbin=int(sys.argv[3])
except:
    nbin=100

try:
    miny=float(sys.argv[4])
    maxy=float(sys.argv[5])
except:
    miny=min(y)
    maxy=max(y)
dy=(maxy-miny)*1.0001/nbin
bin=[0]*nbin
for yy in y:
    j=min(nbin-1,int((yy-miny)/dy))
    bin[j]+=1

normfac=1.0/dy/float(sum(bin))

for j in range(nbin):
    print miny+(j+0.5)*dy, bin[j]*normfac

