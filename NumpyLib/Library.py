import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([1, 2, 3, 4])
a2 = np.zeros(4)
a3 = np.ones(4)
a4 = np.random.random(4)
a5 = np.random.randn(4)
a6 = np.linspace(0, 10, 5)
a7 = np.arange(0, 10, 2)

# print(a7)

# c = 1/a7

# print(c)

# print(a1>2) # Used for numbering the elements in the array

# x = np.linspace(0, 10, 100)
# x**2 + 2*x + 1
# plt.plot(x, x**2 + 2*x + 1)
# plt.show()
# plt.hist(np.random.randn(1000), bins=30)
# plt.show()

# def f(x):
#     return x**2 + 2*np.sin(x) + 1
# x = np.linspace(0, 10, 100)
# y = f(x)
# plt.plot(x, y)
# plt.show()

# a1 = np.array([1, 2, 3, 4])
# a1[2:]

# a1 = [1, 2, 3, 4]

# b = a1[2:]

#boolean indexing
a1 = np.array([1, 2, 3, 4])
print(a1[a1>2])

#true vs false
a1 = np.array([1, 2, 3, 4])
print(a1>2)

