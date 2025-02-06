import numpy as np
from math import pi
from vpython import graph, gcurve, color, rate

g1 = graph(xtitle='x', ytitle='y', width=600, height=400)
f1 = gcurve(color=color.cyan)
f2 = gcurve(color=color.red)

x =[]
xt = 0
num_points = 100 
dx = pi/(2*num_points)

while xt<=pi/2:
    x = x + [xt]
    xt += dx

fold = []
fnew = []

for i in range(len(x)):
    fa = 1- np.sin(x[i]) - np.cos(x[i])
    f2.plot(pos=(x[i],fa))

for i in range(len(x)):
    fold = fold + [0]
    fnew = fnew + [0]
    
n = 0
N = 100
while n<N:
    rate(10)
    f1data = []
    for i in range(1,len(x)-1):
        fnew[i] = 0.5*(fold[i+1]+fold[i-1]-dx**2*(1-fold[i]))
    for i in range(len(x)):
        fold[i] = fnew[i]
    for i in range(len(x)):
        f1data = f1data + [[x[i],fnew[i]]]
    n += 1
    f1.data = f1data
print(fnew)

