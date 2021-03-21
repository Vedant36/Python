import matplotlib.pyplot as plt
import numpy as np
import random as rd

x = np.linspace(-5, 5, 640)
y = x**3

plt.scatter(x, y, color='#ff0000', s=0.1)
plt.show()