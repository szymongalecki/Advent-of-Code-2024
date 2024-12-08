# golfing
with open("input", "r") as f:
    left, right = zip(*[tuple(map(int, line.split())) for line in f.readlines()])
    print(sum(abs(l - r) for (l, r) in zip(sorted(left), sorted(right))))
