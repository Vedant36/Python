
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

n = 20
x, y = 8*np.pi*(np.indices((n, n))-n//2)/n
d = 0.5
z = np.sin(np.hypot(x, y-d)) + np.sin(np.hypot(x, y+d))

surf = ax.plot_surface(x, y, z, antialiased = True, color='#3BBDF7', linewidth=0)#, cmap=cm.coolwarm,  antialiased=False)

# Customize the z axis.
# ax.set_zlim(0., 2.)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
