import sys


def data() -> list[int]:
    return [int(d) for d in open(sys.argv[1], "r").readline()]


def layout(data: list[int]) -> list[int | None]:
    ly = []
    for i, d in enumerate(data):
        if i % 2 == 0:
            ly += [i // 2] * d
        else:
            ly += [None] * d
    return ly


def compact(layout: list[int | None]) -> list[int | None]:
    l = 0
    r = len(layout) - 1
    while l < r:
        if layout[l] is None and layout[r] is not None:
            layout[l], layout[r] = layout[r], layout[l]
        if layout[l] is not None:
            l += 1
        if layout[r] is None:
            r -= 1
    return layout


def checksum(compact: list[int | None]) -> int:
    return sum(i * int(d) for i, d in enumerate(compact) if d)


print(f"Part one: {checksum(compact(layout(data())))}")
