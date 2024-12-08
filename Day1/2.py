with open("input", "r") as f:
    left = set()
    right = dict()
    for line in f.readlines():
        l, r = [int(n) for n in line.split()]
        left.add(l)
        if r in right:
            right[r] += 1
        else:
            right[r] = 1
    print(sum(n * right[n] for n in left if n in right))
