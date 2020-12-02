import csv
from math import log10

M_SUN = 2e+30
C_LIGHT = 299792458
L_SUN = 3.828e+26

solar_masses = [
    25, 15,
    12, 9,
    7, 5,
    4, 3,
    2.5, 2,
    1.5, 1.25,
    1, 0.8
]
masses = [i * M_SUN for i in solar_masses]

en = lambda m: 0.1 * 0.007 * m * C_LIGHT**2
energies = list(map(en, masses))

times = [
    6.40774, 11.5842,
    16.0176, 26.3886,
    43.1880, 94.4591,
    164.734, 352.503,
    584.916, 1115.94,
    2690.39, 4910.11,
    9844.57, 25027.9
]
lum = lambda et: et[0] / (et[1] * 10**6 * 365 * 86400 * L_SUN)
luminosities = list(map(lum, zip(energies, times)))
log_lum = list(map(log10, luminosities))
log_m = list(map(log10, masses))

with open("ps10/q2.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["mass", "energy", "luminosity", "log-lum", "log-m"])
    for i, j, k, l, m in zip(solar_masses, energies, luminosities, log_lum, log_m):
        writer.writerow(list(map(str, [i, j, k, l, m])))
