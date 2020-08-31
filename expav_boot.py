#!/usr/bin/env python
import numpy,random,sys

#Usage: expav_boot.py datafile [kt  [nboot] ]

if len(sys.argv)>2:
    kt=float(sys.argv[2])
else:
    kt=2.5

if len(sys.argv)>3:
    nboot=int(sys.argv[3])
else:
    nboot=100


dat=[float(x) for x in open(sys.argv[1]).readlines()]
n=len(dat)
s=0
s2=0
sc=0
sc2=0
sa=0
sa2=0
for ib in range(nboot):
    d=[]
    for i in range(n) :
        j = random.randint(0,n-1)
        d.append(dat[j])
    m=min(d)
    fe=-kt*numpy.log(sum([numpy.exp(-(e-m)/kt) for e in d])/n)+m
    av=sum([(e-m) for e in d])/n
    var=sum([(e-m)**2 for e in d])/n-av**2
    av+=m
    #print av, numpy.sqrt(var),av-var/(2*kt), fe
    cumfe=av-var/(2*kt)
    s+=fe
    s2+=fe**2
    sc+=cumfe
    sc2+=cumfe**2
    sa+=av
    sa2+=av**2

print s/nboot, numpy.sqrt(s2/nboot-(s/nboot)**2)," Using 2nd order cumulant: ", sc/nboot, numpy.sqrt(sc2/nboot-(sc/nboot)**2), "Using plain av: ", sa/nboot, numpy.sqrt(sa2/nboot-(sa/nboot)**2)
