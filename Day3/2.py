import re

with open("input", "r") as f:
    text = f.read()
    pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
    matches = re.findall(pattern, text)
    add = True
    result = 0
    for m in matches:
        if m == "do()":
            add = True
        elif m == "don't()":
            add = False
        else:
            if add:
                a, b = m.removeprefix("mul(").removesuffix(")").split(",")
                result += int(a) * int(b)
    print(result)
