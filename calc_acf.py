#!/usr/bin/env python

#Usage: calc_acf file [colnr [ndiscard] ]

import sys
from numpy import *

if len(sys.argv)>2:
  colnr=int(sys.argv[2])
else:
  colnr=1

if len(sys.argv)>3:
  ndiscard=int(sys.argv[3])
else:
  ndiscard=0

lines=[line for line in open(sys.argv[1]).readlines() if line[0]!='#']
f=array([float(line.split()[colnr-1]) for line in lines[ndiscard:]])
f-=f.mean()
N=len(f)
for t in range(N/2):
   print t, sum(f[0:(N-t)]*f[t:N])/sum(f[0:(N-t)]**2)

