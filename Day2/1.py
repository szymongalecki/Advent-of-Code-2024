def safe(report):
    asc = False
    desc = False
    for a, b in zip(report[:-1], report[1:]):
        if b - a > 0:
            asc = True
        if b - a < 0:
            desc = True
        if asc == True and desc == True:
            return False
        if abs(b - a) < 1 or abs(b - a) > 3:
            return False
    return True


with open("input", "r") as f:
    safe_reports = 0
    for line in f.readlines():
        report = [int(n) for n in line.split()]
        if safe(report):
            safe_reports += 1
    print(safe_reports)