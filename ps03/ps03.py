import numpy as np
import csv

wl_bins = np.linspace(1000, 10000, 11)
num_bins = 10
h, c = 6.62607015e-27, 299782458
f_bins = np.linspace(c / (wl_bins[0] * 10e-10), c / (wl_bins[-1] * 10e-10), 11)
print(f_bins)

with open('ps03/3a.csv', 'w') as d1, open('ps03/3b.csv', 'w') as d2:
    fields = ['wl', 'f']
    writer1, writer2 = csv.DictWriter(d1, fields), csv.DictWriter(d2, fields)
    writer1.writeheader()
    writer2.writeheader()
    for i in range(num_bins):
        f_wl = 90 / (20000 * 50)
        writer1.writerow({
            fields[0]: wl_bins[i],
            fields[1]: f_wl
        })
        div = f_bins[i] - f_bins[i + 1]
        f_freq = (h * div) / (20000 * 50)
        print(f_freq)
        writer2.writerow({
            fields[0]: f_bins[i],
            fields[1]: f_freq
        })
    writer1.writerow({
        fields[0]: wl_bins[-1],
        fields[1]: f_wl
    })
    div = f_bins[-2] - f_bins[-1]
    f_freq = (h * div) / (20000 * 50)
    writer2.writerow({
        fields[0]: f_bins[-1],
        fields[1]: f_freq
    })

