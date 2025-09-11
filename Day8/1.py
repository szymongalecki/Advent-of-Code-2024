import sys


def data() -> list[list[str]]:
    return [list(l.strip()) for l in open(sys.argv[1], "r").readlines()]


def antennas(data: list[list[str]]) -> list[tuple[str, int, int]]:
    return [
        (f, y, x) for y, row in enumerate(data) for x, f in enumerate(row) if f != "."
    ]


def antinodes(antennas: list[tuple[str, int, int]]) -> list[tuple[int, int]]:
    return [
        coordinates
        for id1, (f1, y1, x1) in enumerate(antennas)
        for id2, (f2, y2, x2) in enumerate(antennas)
        if id1 != id2 and f1 == f2
        for coordinates in [(2 * y1 - y2, 2 * x1 - x2), (2 * y2 - y1, 2 * x2 - x1)]
    ]


def part_one() -> int:
    city = data()
    y_lim, x_lim = len(city), len(city[0])
    return len(
        {
            (y, x)
            for (y, x) in antinodes(antennas(city))
            if 0 <= x < x_lim and 0 <= y < y_lim
        }
    )


print(f"Part one: {part_one()}")
