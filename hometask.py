import numpy as np
import matplotlib.pyplot as mp


def f(x):
    return a * x ** 2 + b * x + c


while True:
    try:
        a, b, c = map(int, input("Please, enter a, b and c for quadratic function - ").split())
        break
    except TypeError:
        pass

log_x, log_y, sq_x, sq_y = [], [], [], []
for i in range(-100, 100):
    log_x.append(i)
    log_y.append(np.log2(i))
    sq_x.append(i)
    sq_y.append(f(i))
mp.plot(log_x, log_y)
mp.plot(sq_x, sq_y)
mp.show()
