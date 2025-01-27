import re

import numpy as np

with open("input", "r") as f:
    arr = np.array([list(c) for c in [l.removesuffix("\n") for l in f.readlines()]])
    horizontal = ["".join(l) for l in arr]
    vertical = ["".join(l) for l in np.transpose(arr)]
    offset = len(arr) - 1
    diagonal = ["".join(arr.diagonal(o)) for o in range(-offset, offset + 1, 1)]
    anti = ["".join(np.fliplr(arr).diagonal(o)) for o in range(-offset, offset + 1, 1)]
    paths = horizontal + vertical + diagonal + anti
    xmas = r"XMAS"
    samx = r"SAMX"
    xmas_matches = sum(len(re.findall(xmas, p)) for p in paths)
    samx_matches = sum(len(re.findall(samx, p)) for p in paths)
    result = xmas_matches + samx_matches
    print(result)
