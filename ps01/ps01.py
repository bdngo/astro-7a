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

log_P = list(map(log10, periods))
log_a = list(map(log10, axes))
print(log_P)
print(log_a)
m, b = np.polyfit(log_P, log_a, 1)
print(m, b)
