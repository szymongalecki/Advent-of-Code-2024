import re

import numpy as np


def xmas(a):
    a = np.array(a)
    for k in range(4):
        r = np.rot90(a, k=k)
        if (
            r[0][0] == "M"
            and r[0][2] == "S"
            and r[1][1] == "A"
            and r[2][0] == "M"
            and r[2][2] == "S"
        ):
            return True
    return False


with open("input", "r") as f:
    arr = np.array([list(c) for c in [l.removesuffix("\n") for l in f.readlines()]])
    result = 0
    for i in range(0, len(arr) - 2):
        for j in range(0, len(arr[i]) - 2):
            a = arr[i : i + 3, j : j + 3]
            if xmas(a):
                result += 1
    print(result)
