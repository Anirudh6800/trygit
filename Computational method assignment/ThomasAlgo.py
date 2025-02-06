# # Thomas algorithm for solving tridiagonal matrix
# import numpy as np

# #Input
# n = 4
# alpha = [0, 1, 2, 3]
# beta = [1, 2, 3, 4]
# gamma = [1, 2, 3, 0]
# b = [1, 2, 3, 4]

# #Elimination
# e = [0, 0 ,0, 0]
# f = [0, 0, 0, 0]
# x = [0]*n #Solution 
# e[0] = -gamma[0]/beta[0]
# f[0] = b[0]/beta[0]

# for j in range(1, n-1):
#     d = (beta[j] - alpha[j]*e[j-1])
#     e[j] = gamma[j]/d 
#     f[j] = (b[j] - alpha[j]*f[j-1])/d
    
# x[n-1] = (alpha[n-1]*f[n-2] + b[n-1])/(alpha[n-1]*e[n-2] -beta[n-1])
# for j in range(n-2, -1, -1):
#     x[j] = f[j] - e[j]*x[j+1]
# print('x =', [round(i, 5) for i in x])

#make a function of thomas algorithm
def thomas(n, alpha, beta, gamma, b):
    e = [0]*n 
    f = [0]*n
    x = [0]*n
    e[0] = -gamma[0]/beta[0]
    f[0] = b[0]/beta[0]
    for j in range(1, n-1):
        d = (beta[j] - alpha[j]*e[j-1])
        e[j] = gamma[j]/d 
        f[j] = (b[j] - alpha[j]*f[j-1])/d
    x[n-1] = (alpha[n-1]*f[n-2] + b[n-1])/(alpha[n-1]*e[n-2] -beta[n-1])
    for j in range(n-2, -1, -1):
        x[j] = f[j] - e[j]*x[j+1]
    return x

#Test the function
n = 4
alpha = [0, 1, 2, 3]
beta = [1, 2, 3, 4]
gamma = [1, 2, 3, 0]
b = [1, 2, 3, 4]
print('x =', [round(i, 5) for i in thomas(n, alpha, beta, gamma, b)])
