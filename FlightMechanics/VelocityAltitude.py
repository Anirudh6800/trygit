
# Plot delta e v/s Cl 
import numpy as np
import matplotlib.pyplot as plt

#Define the parameters
Cl = np.array([0.1632486481,
0.16,
0.153787005,
0.1508153455,
0.1451247166,
0.1423994304,
0.1423994304,
0.1397501965,
0.1397501965,
0.1397501965,
0.1397501965,
0.1423994304,
0.1451247166,
0.1479289941,
0.153787005])

delta_e = np.array([1.16895,
1.16895,
1.16895,
1.09113,
1.16895,
1.16895,
1.16895,
1.09113,
1.09113,
1.01334,
1.09113,
1.01334,
1.01334,
0.93552,
0])
#Plot the results
plt.plot(Cl, delta_e, 'o-')
plt.xlabel('Cl')
plt.ylabel('delta_e')
plt.title('delta_e vs Cl')
plt.show()
