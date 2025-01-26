import re

with open("input", "r") as f:
    text = f.read()
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, text)
    products = [int(x[0]) * int(x[1]) for x in matches]
    result = sum(products)
    print(result)
