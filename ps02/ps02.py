import matplotlib.pyplot as plt
import matplotlib.colors as clr
from matplotlib.patches import Ellipse
from math import sqrt

smajor_axes = [
    9.27e-2,
    1.10e-1,
    1.57e-1,
    1.97e-1,
    2.54e-1,
    4.72e-1
]

eccentricities = [
    0.045,
    0.026,
    0.004,
    0.012,
    0.013,
    0.015
]

sminor_axes = [sqrt(i**2 * (1 - j**2)) for i, j in zip(smajor_axes, eccentricities)]

colors = [
    '#0000ff',
    '#00ff00',
    '#00ffff',
    '#ff0000',
    '#ff00ff',
    '#000000'
]

plt.title("Orbits of Kepler-11")
ax = plt.subplot()
for i, j, k in zip(smajor_axes, sminor_axes, colors):
    ax.add_artist(Ellipse((0, 0), 2*i, 2*j, color=k,fill=False))
plt.xlim((-0.5, 0.5))
plt.ylim((-0.5, 0.5))
plt.xlabel("Semimajor axis [au]")
plt.ylabel("Semiminor axis [au]")
plt.show()
