import numpy as np
import matplotlib.pyplot as plt
#Solve heat equation using finite difference method
alpha = 1

# 1D heat equation: 
# u_t = alpha*u_xx
# Initial condition: x= [0,1] & t = [0,1]
# L= 1
#Discretize the domain:
dx = 0.01
dt = 0.0001
Nx = 100
Nt = 10000

# Define the spatial and temporal domain
x = np.linspace(0, 1, Nx)
t = np.linspace(0, 1, Nt)

# Initial condition
u = np.zeros((Nx, Nt))
u[:, 0] = 20
u[0, :] = 20
u[-1, :] = 100

#Discretize the domain:
#dx = 0.1
#dt = 0.01
#Nx = 10
#Nt = 100



#Initial condition:
u = np.zeros((Nx,Nt))
u[:,0] = 20
u[0,:] = 20
u[-1,:] = 100

#Finite difference method:
for n in range(0,Nt-1):
    for i in range(1,Nx-1):
        u[i,n+1] = u[i,n] + alpha * dt / dx**2 * (u[i+1,n] - 2*u[i,n] + u[i-1,n])
        
#Plot the solution:
plt.plot(u)
plt.xlabel('x')
plt.ylabel('T')
plt.title('Heat equation')
plt.show()



