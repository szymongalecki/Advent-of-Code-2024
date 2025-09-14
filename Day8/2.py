import sys


def data() -> list[list[str]]:
    return [list(l.strip()) for l in open(sys.argv[1], "r").readlines()]


def antennas(data: list[list[str]]) -> list[tuple[str, int, int]]:
    return [
        (f, y, x) for y, row in enumerate(data) for x, f in enumerate(row) if f != "."
    ]


def locations(
    y1: int,
    x1: int,
    y2: int,
    x2: int,
    y_lim: int,
    x_lim: int,
) -> list[tuple[int, int]]:
    l = []
    y_diff = y1 - y2
    x_diff = x1 - x2
    while 0 <= y1 < y_lim and 0 <= x1 < x_lim:
        l.append((y1, x1))
        y1 += y_diff
        x1 += x_diff
    while 0 <= y2 < y_lim and 0 <= x2 < x_lim:
        l.append((y2, x2))
        y2 -= y_diff
        x2 -= x_diff
    return l


def antinodes(
    antennas: list[tuple[str, int, int]],
    y_lim: int,
    x_lim: int,
) -> list[tuple[int, int]]:
    a = []
    for id1, (f1, y1, x1) in enumerate(antennas):
        for id2, (f2, y2, x2) in enumerate(antennas):
            if id1 != id2 and f1 == f2:
                a += locations(y1, x1, y2, x2, y_lim, x_lim)
    return a


def part_two() -> int:
    # absolutely disgusting composition ;)
    return len(set(antinodes(antennas(data()), len(data()), len(data()[0]))))


print(f"Part two: {part_two()}")
