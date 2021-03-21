# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 200)
z = np.arange(200)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
print(x.shape)
print(y.shape)
print(z.shape)

ax.plot(x, y, r, label='graph boi')
ax.plot(x, -y, r, label='graph boi')
ax.plot(-x, y, r, label='graph boi')
ax.plot(-x, -y, r, label='graph boi')
ax.legend()
plt.show()
