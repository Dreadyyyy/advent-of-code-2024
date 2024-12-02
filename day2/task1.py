def is_safe(r: list[int]) -> bool:
    if len(r) <= 1:
        return True
    if len(r) == 2:
        return 1 <= abs(r[0] - r[1]) <= 3

    for x1, x2, x3 in zip(r, r[1:], r[2:]):
        if not (
            (x1 < x2 < x3 or x1 > x2 > x3)
            and 1 <= abs(x1 - x2) <= 3
            and 1 <= abs(x2 - x3) <= 3
        ):
            return False
    return True


with open("input.txt") as f:
    reports = [list(map(int, l.split(" "))) for l in f.readlines()]

res = sum(is_safe(r) for r in reports)
print(res)
