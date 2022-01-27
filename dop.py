
from numba import njit
import random
import numpy as np


@njit(fastmath=True, cache=True)
def generateMap(w, h):
    ley = [5, 20, 50, 100, 150, 200]

    a = np.zeros((w, h))
    aLine = np.zeros((w, h))

    for s in ley:
        for i in range(0, w, s):
            for j in range(0, h, s):
                r = int(random.random() * 10) / 10
                for i0 in range(s):
                    for j0 in range(s):
                        aLine[i + i0][j + j0] = r
        a += aLine

    a = toColor(sglaj(a * (255.0 / len(ley)), w, h), w, h)

    return a


@njit(fastmath=True, cache=True)
def sglaj(a, w, h):
    k = 6
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            a[i][j] = (a[i][j] + k * a[i - 1][j] + k * a[i][j - 1]) / (2 * k + 1)
    for i in range(w - 2, 1, -1):
        for j in range(h - 2, 1, -1):
            a[i][j] = (a[i][j] + k * a[i + 1][j] + k * a[i][j + 1]) / (2 * k + 1)
    for i in range(1, w - 1):
        for j in range(h - 2, 1, -1):
            a[i][j] = (a[i][j] + k * a[i - 1][j] + k * a[i][j + 1]) / (2 * k + 1)
    for i in range(w - 2, 1, -1):
        for j in range(1, h - 1):
            a[i][j] = (a[i][j] + k * a[i + 1][j] + k * a[i][j - 1]) / (2 * k + 1)

    return a


@njit(fastmath=True, cache=True)
def toColor(a, w, h):
    aNew = np.zeros((w, h, 3), np.int64)
    for i in range(10, w-10):
        for j in range(h):
            k = a[i][j]
            if k > 155.0:
                k = int(k - 155)*3
                color = [150-k, 120-k, 0]
            elif k > 120.0:
                color = [50, 170, 50]
            elif k > 115.0:
                color = [200, 200, 50]
            else:
                k = int(k - 70) if k > 70 else 0
                color = [k, 50 + k, 150 + k]

            aNew[i-10][j] = color

    return aNew