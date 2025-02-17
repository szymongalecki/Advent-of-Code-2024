def guard_position(arr):
    for y, row in enumerate(arr):
        for x, _ in enumerate(row):
            if arr[y][x] in {"<", ">", "^", "v"}:
                return x, y


def guard_direction(arr):
    for y, row in enumerate(arr):
        for x, _ in enumerate(row):
            match arr[y][x]:
                case "<":
                    return (-1, 0)
                case ">":
                    return (1, 0)
                case "^":
                    return (0, 1)
                case "v":
                    return (0, -1)


def turn_90(x_dir, y_dir):
    match (x_dir, y_dir):
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)
        case (-1, 0):
            return (0, 1)


def walk(arr, x, y, x_dir, y_dir, count):
    if y == len(arr) - 1 or x == len(arr[0]) - 1:
        return count
    if arr[y + y_dir][x + x_dir] == "#":
        x_dir, y_dir = turn_90(x_dir, y_dir)
    elif arr[y + y_dir][x + x_dir] == "X":
        walk(arr, x + x_dir, y + y_dir, x_dir, y_dir, count)
    elif arr[y + y_dir][x + x_dir] == ".":
        arr[y + y_dir][x + x_dir] = "X"
        print(
            f"guard: {arr[y][x]}, x: {x + x_dir}, y: {y + y_dir}, x_dir: {x_dir}, y_dir: {y_dir}, count: {count+1}"
        )
        walk(arr, x + x_dir, y + y_dir, x_dir, y_dir, count + 1)
    else:
        print("Unexpected event")


with open("example", "r") as f:
    arr = [list(_.strip()) for _ in f.readlines()]
    x, y = guard_position(arr)
    x_dir, y_dir = guard_direction(arr)
    print(f"guard: {arr[y][x]}, x: {x}, y: {y}, x_dir: {x_dir}, y_dir: {y_dir}")
    arr[y][x] = "X"
    print(walk(arr, x, y, x_dir, y_dir, 1))
