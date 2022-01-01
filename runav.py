#!/usr/bin/python

#Usage: runav.py file.xvg length
import sys



N=int(sys.argv[2])
v=[[float(y) for y in x.split()] for x in open(sys.argv[1]).readlines() if x[0]!='#' and x[0]!='@']
n=len(v[0])-1
for i in range(N-1,len(v)):
    s=[0.0]*n
    for j in range(N):
        for k in range(n): s[k]+=v[i-j][k+1]
    print v[i-N/2][0]," ".join(["%f"%(x/N) for x in s])
