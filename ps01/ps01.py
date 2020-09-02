import matplotlib.pyplot as plt
import numpy as np
from math import log10

periods = [
    1.511,
    2.422,
    4.049,
    6.099,
    9.206,
    12.364,
    18.768
]
axes = [
    0.0115,
    0.0158,
    0.0222,
    0.0292,
    0.0384,
    0.0467,
    0.0617
]
letters = "bcdefgh"

m, b = np.polyfit(list(map(log10, periods)), list(map(log10, axes)), 1)
print(m, b)

plt.subplots_adjust(left=0.2)
plt.xscale('log', basex=10)
plt.yscale('log', basey=10)
plt.xlabel('log(P) [d]')
plt.ylabel('log(a) [au]')
plt.title('Log-log plot of Period vs. Semimajor Axis')
for i in range(len(letters)):
    plt.annotate(letters[i], (periods[i], axes[i]))

plt.plot(periods, axes, 'ro', periods, axes)
plt.show()
