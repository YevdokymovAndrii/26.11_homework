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

