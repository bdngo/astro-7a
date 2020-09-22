import numpy as np
import csv

num_bins = 10
c = 29978245800
wl_bins = 1e-8 * np.linspace(1000, 10000, 11)
delta_wl = wl_bins[1] - wl_bins[0]
f_bins = np.linspace(c / wl_bins[-1], c / wl_bins[0], 11)
delta_f = f_bins[1] - f_bins[0]
f_energy = []

with open('ps03/4a.csv', 'w') as d1, open('ps03/4b.csv', 'w') as d2:
    fields = ['wl', 'f']
    writer1, writer2 = csv.DictWriter(d1, fields), csv.DictWriter(d2, fields)
    writer1.writeheader()
    writer2.writeheader()
    f_wl = 90 / (20000 * 50 * delta_wl)
    for i in range(num_bins):
        writer1.writerow({
            fields[0]: wl_bins[i],
            fields[1]: f_wl
        })
        f_divs = f_bins[0] + i * delta_f
        f_freq = f_wl * (delta_wl / f_divs)
        writer2.writerow({
            fields[0]: f_bins[i],
            fields[1]: f_freq
        })
        f_energy.append(f_freq * delta_f)
    writer1.writerow({
        fields[0]: wl_bins[-1],
        fields[1]: f_wl
    })
    f_divs = f_bins[0] + (num_bins) * delta_f
    f_freq = f_wl * (delta_wl / f_divs)
    writer2.writerow({
        fields[0]: f_bins[-1],
        fields[1]: f_freq
    })
    f_energy.append(f_freq * delta_f)
    print(20000 * 50 * sum(f_energy))
