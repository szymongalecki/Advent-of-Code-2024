import sys


def data() -> list[tuple[int, list[int]]]:
    with open(sys.argv[1], "r") as f:
        return [
            (l[0], l[1:])
            for l in [
                list(map(int, l.strip().replace(":", "").split()))
                for l in f.readlines()
            ]
        ]


def calibrated(value: int, numbers: list[int], index: int, temp: int) -> bool:
    if index == len(numbers):
        if temp == value:
            return True
        else:
            return False
    return calibrated(value, numbers, index + 1, temp + numbers[index]) or calibrated(
        value, numbers, index + 1, temp * numbers[index]
    )


def concatenate(a: int, b: int) -> int:
    return int(str(a) + str(b))


def recalibrated(value: int, numbers: list[int], index: int, temp: int) -> bool:
    if index == len(numbers):
        if temp == value:
            return True
        else:
            return False
    return (
        recalibrated(value, numbers, index + 1, temp + numbers[index])
        or recalibrated(value, numbers, index + 1, temp * numbers[index])
        or recalibrated(value, numbers, index + 1, concatenate(temp, numbers[index]))
    )


def part_one() -> int:
    result = 0
    for value, numbers in data():
        if calibrated(value, numbers, 1, numbers[0]):
            result += value
    return result


def part_two() -> int:
    result = 0
    for value, numbers in data():
        if recalibrated(value, numbers, 1, numbers[0]):
            result += value
    return result


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
