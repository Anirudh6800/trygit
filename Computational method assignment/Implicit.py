#following the algo
# Boundary conditions:

#  1. T(x,t = 0) = 20
# T(x = 0,t) = 20
# T(x = 1,t) = 100
# α = 1

#  2. T(x,t = 0) = 6sin(πx/L)
# T(x = 0,t) = 0
# T(x = 1,t) = 0
# α = 1

#  Take ∆x = 0.1. Select ∆t such the β = α∆t/∆x = 0.3, 0.4, 0.5, 0.6, 0.7


# Use Thomas algorithm for implicit method.

import numpy as np
import matplotlib.pyplot as plt


# Use Thomas algorithm for implicit method
def thomas_algorithm(a, b, c, d):
    n = len(d)
    e = np.zeros(n)
    f = np.zeros(n)
    x = np.zeros(n)
    e[0] = -c[0]/b[0]
    f[0] = d[0]/b[0]
    for j in range(1, n-1):
        d1 = (b[j] - a[j]*e[j-1])
        e[j] = c[j]/d1
        f[j] = (d[j] - a[j]*f[j-1])/d1
    x[n-1] = f[n-1]
    for j in range(n-2, -1, -1):
        x[j] = f[j] - e[j]*x[j+1]
    return x

#Define the parameters
L = 1
alpha = 1
dx = 0.1
dt = 0.1
x = np.arange(0, L+dx, dx)
t = np.arange(0, 1+dt, dt)
boundary_conditions = [0, 0]
initial_conditions = 6*np.sin(np.pi*x/L)
n = len(x)
m = len(t)
T = np.zeros((n, m))
T[0, :] = boundary_conditions[0]
T[-1, :] = boundary_conditions[1]
T[:, 0] = initial_conditions
beta = alpha*dt/dx**2
A = np.diag([1+2*beta]*n, 0) + np.diag([-beta]*(n-1),-1) + np.diag([-beta]*(n-1), 1)
for j in range(1, m):
    b = T[:, j-1].copy()
    b[0] = boundary_conditions[0]
    b[-1] = boundary_conditions[1]
    T[:, j] = thomas_algorithm(np.full(n-1, -beta), np.full(n, 1 + 2*beta), np.full(n-1, -beta), b)

#Plot the results
plt.figure(figsize=(10, 5))
plt.plot(x, T[:, 0], label='t=0s')
plt.plot(x, T[:, 1], label='t=0.1s')
plt.plot(x, T[:, 2], label='t=0.2s')
plt.plot(x, T[:, 3], label='t=0.3s')
plt.plot(x, T[:, 4], label='t=0.4s')
plt.plot(x, T[:, 5], label='t=0.5s')
plt.plot(x, T[:, 6], label='t=0.6s')
plt.plot(x, T[:, 7], label='t=0.7s')
plt.plot(x, T[:, 8], label='t=0.8s')
plt.plot(x, T[:, 9], label='t=0.9s')
plt.plot(x, T[:, 10], label='t=1s')   
plt.xlabel('x')
plt.ylabel('T')
plt.title('Heat Equation')
plt.legend()
plt.grid()
plt.show()



