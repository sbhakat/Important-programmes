#!/usr/bin/python
from numpy import genfromtxt
from numpy import corrcoef
import sys
data = genfromtxt(sys.argv[1])
first=int(sys.argv[2])
second=int(sys.argv[3])

r = corrcoef(data[1:,first-1],data[1:,second-1])[0,1]
print("%.3f %.3f" % (r,r**2))
