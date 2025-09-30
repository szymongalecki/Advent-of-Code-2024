import sys

sys.setrecursionlimit(10**5)


def data() -> list[int]:
    return [int(d) for d in open(sys.argv[1], "r").readline()]


def layout(data: list[int]) -> list[tuple]:
    ly = []
    for i, d in enumerate(data):
        if d == 0:
            continue
        if i % 2 == 0:
            ly.append((i // 2, d))
        else:
            ly.append((None, d))
    return ly


def compact_recursive(layout: list[tuple], tail: list[tuple]):
    if not layout:
        return tail
    if layout[-1][0] is not None:
        file_value, file_size = layout[-1]
        for s, (space_value, space_size) in enumerate(layout):
            if space_value is not None:
                continue
            if space_size < file_size:
                continue
            if space_size == file_size:
                layout[s], layout[-1] = layout[-1], layout[s]
                return compact_recursive(layout, tail)
            if space_size > file_size:
                layout[-1] = (space_value, file_size)
                left, right = layout[:s], layout[s + 1 :]
                left += [
                    (file_value, file_size),
                    (space_value, space_size - file_size),
                ]
                layout = left + right
                return compact_recursive(layout, tail)
    tail = [layout[-1]] + tail
    del layout[-1]
    return compact_recursive(layout, tail)


def flatten(compact: list[tuple]) -> list[int | None]:
    result = []
    for value, size in compact:
        for _ in range(size):
            result.append(value)
    return result


def checksum(compact: list[int | None]) -> int:
    return sum(i * int(d) for i, d in enumerate(compact) if d)


print(f"Part two: {checksum(flatten(compact_recursive(layout(data()), [])))}")
