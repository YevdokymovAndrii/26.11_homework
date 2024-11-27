import numpy as np
import matplotlib.pyplot as mp
from shapely.geometry import LineString


def f(x):
    return a * x ** 2 + b * x + c

while True:
    try:
        a, b, c = map(int, input("Please, enter a, b and c for quadratic function - ").split())
        break
    except ValueError:
        pass

log_x, log_y, sq_x, sq_y, x, y, a_y = [], [], [], [], [], [], []


for i in range(-1500, 1500):
    if i > 0:
        log_x.append(i/100)
        log_y.append(np.log2(i/100))
    sq_x.append(i/100)
    sq_y.append(f(i/100))

mp.plot(log_x, log_y)
mp.plot(sq_x, sq_y)


line_1 = LineString(np.column_stack((log_x, log_y)))
line_2 = LineString(np.column_stack((sq_x, sq_y)))
intersection = line_1.intersection(line_2)

mp.plot(intersection.x, intersection.y)
print(f"intersection points: {intersection}")

mp.show()
