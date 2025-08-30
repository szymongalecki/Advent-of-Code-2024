import sys
from typing import List, Tuple

sys.setrecursionlimit(100000)


def guard_position(arr: List[List[str]]):
    for y, row in enumerate(arr):
        for x, _ in enumerate(row):
            if arr[y][x] in {"<", ">", "^", "v"}:
                return (x, y)


def guard_direction(arr: List[List[str]]):
    for y, row in enumerate(arr):
        for x, _ in enumerate(row):
            match arr[y][x]:
                case "<":  # left
                    return (-1, 0)
                case ">":  # right
                    return (1, 0)
                case "^":  # up
                    return (0, -1)
                case "v":  # down
                    return (0, 1)


def turn_90(x_dir: int, y_dir: int):
    match (x_dir, y_dir):
        case (0, -1):  # up to right
            return (1, 0)
        case (1, 0):  # right to down
            return (0, 1)
        case (0, 1):  # down to left
            return (-1, 0)
        case (-1, 0):  # left to up
            return (0, -1)


def walk(arr: List[List[str]], x: int, y: int, x_dir: int, y_dir: int, count: int):
    if y == 0 or y == len(arr) - 1 or x == 0 or x == len(arr) - 1:
        # guard is leaving the mapped area
        return count
    if arr[y + y_dir][x + x_dir] == "#":
        # guard turned 90 degrees after reaching obstacle
        x_dir, y_dir = turn_90(x_dir, y_dir)
        return walk(arr, x, y, x_dir, y_dir, count)
    elif arr[y + y_dir][x + x_dir] == "X":
        # guard already visited this position
        return walk(arr, x + x_dir, y + y_dir, x_dir, y_dir, count)
    elif arr[y + y_dir][x + x_dir] == ".":
        # guard visited this position for the first time
        arr[y + y_dir][x + x_dir] = "X"
        # print(f"x: {x + x_dir}, y: {y + y_dir}, x_dir: {x_dir}, y_dir: {y_dir}, count: {count+1}")
        return walk(arr, x + x_dir, y + y_dir, x_dir, y_dir, count + 1)


with open("example", "r") as f:
    arr = [list(_.strip()) for _ in f.readlines()]
    x, y = guard_position(arr)
    x_dir, y_dir = guard_direction(arr)
    arr[y][x] = "X"
    print(walk(arr, x, y, x_dir, y_dir, 1))
