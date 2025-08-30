import sys


def guard_position(arr: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(arr):
        for x, _ in enumerate(row):
            if arr[y][x] in {"<", ">", "^", "v"}:
                return (x, y)
    raise Exception("Guard position not found!")


def arrow_to_direction(arrow: str) -> tuple[int, int]:
    return {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}[arrow]


def turn_90(x_dir: int, y_dir: int) -> tuple[int, int]:
    return (-1 * y_dir, x_dir)


def walk(
    arr: list[list[str]],
    x: int,
    y: int,
    x_dir: int,
    y_dir: int,
) -> tuple[int, int, int, int] | None:
    if (
        x + x_dir < 0
        or x + x_dir >= len(arr[0])
        or y + y_dir < 0
        or y + y_dir >= len(arr)
    ):
        return None
    if arr[y + y_dir][x + x_dir] == "#":
        x_dir, y_dir = turn_90(x_dir, y_dir)
        return (x, y, x_dir, y_dir)
    return (x + x_dir, y + y_dir, x_dir, y_dir)


def loop(
    arr: list[list[str]],
    x: int,
    y: int,
    x_dir: int,
    y_dir: int,
) -> bool:
    visited: set[tuple[int, int, int, int]] = set()
    while True:
        if (x, y, x_dir, y_dir) in visited:
            return True
        visited.add((x, y, x_dir, y_dir))
        valid_walk = walk(arr, x, y, x_dir, y_dir)
        if not valid_walk:
            return False
        x, y, x_dir, y_dir = valid_walk


def obstruct(arr: list[list[str]]):
    for y, row in enumerate(arr):
        for x, _ in enumerate(row):
            if arr[y][x] == ".":
                obstructed = [row.copy() for row in arr]
                obstructed[y][x] = "#"
                yield obstructed


def result() -> int:
    with open(sys.argv[1], "r") as f:
        arr = [list(_.strip()) for _ in f.readlines()]
        x, y = guard_position(arr)
        x_dir, y_dir = arrow_to_direction(arr[y][x])
        return sum(loop(obstructed, x, y, x_dir, y_dir) for obstructed in obstruct(arr))


print(result())
