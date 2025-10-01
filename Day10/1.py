import sys


def topography() -> list[list[int]]:
    return [
        [int(d) for d in list(l.strip())] for l in open(sys.argv[1], "r").readlines()
    ]


def move(
    topography: list[list[int]],
    y_x: tuple[int, int],
    height_prev: int,
) -> None | tuple[int, int] | list:
    y, x = y_x
    y_max, x_max = len(topography), len(topography[0])
    if not (0 <= y < y_max):
        return
    if not (0 <= x < x_max):
        return
    peak, height_diff = 9, 1
    height_curr = topography[y][x]
    if height_curr - height_prev != height_diff:
        return
    if height_curr == peak:
        return y_x
    return [
        move(topography, (y + 1, x), height_curr),
        move(topography, (y - 1, x), height_curr),
        move(topography, (y, x + 1), height_curr),
        move(topography, (y, x - 1), height_curr),
    ]


def flatten(deep: list):
    for d in deep:
        if d is None:
            continue
        if type(d) is tuple:
            yield d
            continue
        try:
            yield from flatten(d)
        except TypeError:
            yield d


def trailheads_scores_sum() -> int:
    trailheads = []
    for y, row in enumerate(topography()):
        for x, height in enumerate(row):
            if height != 0:
                continue
            score = len(set(list(flatten(move(topography(), (y, x), -1)))))  # type: ignore
            trailheads.append(score)
    return sum(trailheads)


print(f"Part one: {trailheads_scores_sum()}")
