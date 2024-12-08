from math import gcd


def check(x: int, y: int, points: list[tuple[int, int]]) -> bool:
    for i, (x1, y1) in enumerate(points[:-1]):
        for x2, y2 in points[i + 1 :]:
            dx1, dy1 = x - x1, y - y1
            dx1, dy1 = dx1 // (n := gcd(dx1, dy1)), dy1 // n

            dx2, dy2 = x1 - x2, y1 - y2
            dx2, dy2 = dx2 // (n := gcd(dx2, dy2)), dy2 // n

            if (dx1, dy1) == (dx2, dy2) or (-dx1, -dy1) == (dx2, dy2):
                return True

    return False


def is_antinode(mp: list[str], x: int, y: int) -> bool:
    pos = {}
    for i, s in enumerate(mp):
        for j, c in enumerate(s):
            if c == ".":
                continue

            pos.setdefault(c, []).append((i, j))

    return (
        any(check(x, y, v) for v in pos.values())
        if (c := mp[x][y]) == "."
        else len(pos[c]) > 1
    )


with open("input.txt") as f:
    mp = [s.strip("\n") for s in f.readlines()]

res = sum(is_antinode(mp, x, y) for x in range(len(mp)) for y in range(len(mp[0])))
print(res)
