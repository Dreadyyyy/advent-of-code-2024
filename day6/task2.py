# bruteforce
def has_cycle(mp: list[list[str]], x: int, y: int) -> bool:
    directions = [[set() for _ in row] for row in mp]
    i, j = -1, 0
    while 0 <= x < len(mp) and 0 <= y < len(mp[0]):
        if (i, j) in directions[x][y]:
            return True

        if mp[x][y] != "#":
            directions[x][y].add((i, j))
            x, y = x + i, y + j
            continue

        x, y = x - i, y - j
        i, j = j, -i
        x, y = x + i, y + j
    return False


with open("input.txt") as f:
    mp = [list(l.strip("\n")) for l in f.readlines()]

x, y = 0, 0
for r, l in enumerate(mp):
    if "^" in l and (c := l.index("^")) != -1:
        x, y = r, c

res = 0
for r in range(len(mp)):
    for c in range(len(mp[0])):
        if mp[r][c] not in ("#", "^"):
            mp[r][c] = "#"
            res += has_cycle(mp, x, y)
            mp[r][c] = "."

print(res)
