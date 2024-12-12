def region(
    mp: list[str], visited: set[tuple[int, int]], curr: str, x: int, y: int
) -> tuple[int, int]:
    if not 0 <= x < len(mp) or not 0 <= y < len(mp[0]) or mp[x][y] != curr:
        return 0, 1

    if (x, y) in visited:
        return 0, 0

    visited.add((x, y))
    rec = [
        region(mp, visited, curr, x + i, y + j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if (i ^ j) and (not i or not j)
    ]

    return 1 + sum(a for a, _ in rec), sum(p for _, p in rec)


with open("input.txt") as f:
    mp = [l.strip("\n") for l in f.readlines()]


visited = set()
res = sum(
    a * p
    for a, p in [
        region(mp, visited, mp[x][y], x, y)
        for x in range(len(mp))
        for y in range(len(mp[0]))
    ]
)

print(res)
