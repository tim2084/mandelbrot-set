import math
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

x_min = -2
x_max = 1
y_min = -1.5
y_max = 1.5
radius = 2
resolution = 0.001
iterations = 128
x_n = int((x_max - x_min) / resolution)
y_n = int((y_max - y_min) / resolution)

xs = np.linspace(x_min, x_max, x_n+1, endpoint=True)
ys = np.linspace(y_min, y_max, y_n+1, endpoint=True)

diverge_after = [[0] * (y_n + 1) for i in range(x_n + 1)]

x = x_min
y = y_min


def iterate(a, b):
    z_a = 0
    z_b = 0
    i = 0
    count = 0
    end = False
    while i < iterations and not end:
        z_a_old = z_a
        z_b_old = z_b
        z_a = z_a_old*z_a_old - z_b_old*z_b_old + a
        z_b = z_a_old*z_b_old + z_b_old*z_a_old + b
        r = math.sqrt(z_a*z_a + z_b*z_b)
        if r <= radius:
            count += 1
        else:
            end = True
        i += 1
    return count


for i in range(y_n + 1):
    for j in range(x_n + 1):
        diverge_after[i][j] = iterate(x, y)
        x += resolution
    x = x_min
    y += resolution
    if i % 100 == 0:
        progress = 100 * (i + 1) / (y_n + 1)
        print("%.2f" % progress, "%")

x_value, y_value = np.meshgrid(xs, ys)

fig, ax = plt.subplots(figsize=(15, 15), dpi=100)
#ax.pcolormesh(xs, ys, diverge_after, cmap=cm.RdGy)
ax.imshow(diverge_after, cmap=cm.RdGy)
#ax.set_aspect(1)
ax.set_axis_off()
fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
#plt.show()
plt.savefig(fname='figure.png')
