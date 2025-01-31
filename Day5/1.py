def correct(update, dependencies):
    for i, x in enumerate(update):
        for y in update[:i]:
            if x in dependencies and y in dependencies[x]:
                return False
    return True


with open("input", "r") as f:
    input = f.read().split()
    updates = [[int(_) for _ in _.split(",")] for _ in input if "," in _]
    rules = [[int(_) for _ in _.split("|")] for _ in input if "|" in _]
    dependencies = dict()
    for r in rules:
        if r[0] not in dependencies:
            dependencies[r[0]] = {r[1]}
        else:
            dependencies[r[0]].add(r[1])
    result = sum([u[(len(u) - 1) // 2] for u in updates if correct(u, dependencies)])
    print(result)
