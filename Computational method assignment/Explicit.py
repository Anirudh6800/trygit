#Solve Heat Equation in 1D using Explicit Finite Difference Method
import numpy as np
import matplotlib.pyplot as plt

#Solve the 1-D heat equation in the domain [0,1] over the period t=0s to t=1s. 
# (L=1)

#Define the parameters
L = 1
alpha = 1
dx = 0.1
dt = 0.1
beta = alpha*dt/dx

#Define the initial conditions
def initial_conditions(x):
    return 6*np.sin(np.pi*x/L)

#Define the boundary conditions
def boundary_conditions(t):
    return 0

# Use second order central difference in space and forward Euler in time.
#Define the grid
x = np.arange(0, L+dx, dx)
t = np.arange(0, 1+dt, dt)
u = np.zeros((len(t), len(x)))
u[0] = initial_conditions(x)

#Use explicit finite difference method to solve the heat equation
for n in range(0, len(t)-1):
    for i in range(1, len(x)-1):
        u[n+1, i] = u[n, i] + beta*(u[n, i-1] - 2*u[n, i] + u[n, i+1])
    u[n+1, 0] = boundary_conditions(t[n+1])
    u[n+1, -1] = boundary_conditions(t[n+1])
    
#Plot the solution
plt.plot(x, u[0], label='t=0')
plt.plot(x, u[1], label='t=0.25')
plt.plot(x, u[2], label='t=0.5')
plt.plot(x, u[3], label='t=0.75')
plt.plot(x, u[4], label='t=1')
plt.xlabel('Distance [m]')
plt.ylabel('Temperature [C]')
plt.legend()
plt.show()



# h = 0.025
# k = 0.025
# x = np.arange(0, 1+h, h)
# t = np.arange(0, 0.1+k, k)

# boundaryConditions = [0,0]
# initialConditions = np.sin(np.pi*x)

# n = len(x)
# m = len(t)
# T = np.zeros((n,m))
# T[0,:] = boundaryConditions[0]
# T[-1,:] = boundaryConditions[1]
# T[:,0] = initialConditions

# print(T.round(3))

# factor = k/h**2

# for j in range(1, m):
#     for i in range(1, n-1):
#         T[i,j] = factor*T[i-1, j-1] + (1-2*factor)*T[i,j-1] + factor*T[i+1,j-1] 
# print(T.round(3))   
# plt.plot(x, T[:,0], label='t=0')
# plt.plot(x, T[:,1], label='t=0.25')
# plt.plot(x, T[:,2], label='t=0.5')
# plt.plot(x, T[:,3], label='t=0.75')
# plt.plot(x, T[:,4], label='t=1')
# plt.xlabel('distance[m]')
# plt.ylabel('Temperature[C]')
# plt.legend()
# plt.show()
   
