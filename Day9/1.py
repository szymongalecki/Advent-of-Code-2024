import sys


def data() -> list[int]:
    return [int(d) for d in open(sys.argv[1], "r").readline()]


def layout(data: list[int]) -> str:
    ly = ""
    for i, d in enumerate(data):
        if i % 2 == 0:
            # fix: breaks layout for digits bigger than 9
            ly += str(i // 2) * d
        else:
            ly += "." * d
    return ly


def compact(layout: str) -> str:
    ly = list(layout)
    l = 0
    r = len(ly) - 1
    while l < r:
        if ly[l] == "." and ly[r] != ".":
            ly[l], ly[r] = ly[r], ly[l]
        if ly[l] != ".":
            l += 1
        if ly[r] == ".":
            r -= 1
    return "".join(ly)


def checksum(compact: str) -> int:
    return sum(i * int(d) for i, d in enumerate(list(compact)) if d != ".")


example = [int(d) for d in "2333133121414131402"]
assert layout(example) == "00...111...2...333.44.5555.6666.777.888899"
assert compact(layout(example)) == "0099811188827773336446555566.............."
assert checksum(compact(layout(example))) == 1928

print(f"Part one: {checksum(compact(layout(data())))}")
