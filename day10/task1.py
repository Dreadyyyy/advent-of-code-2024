directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(
    mp: list[list[int]], visited: set[tuple[int, int]], x: int, y: int, prev: int
) -> int:
    if mp[x][y] != prev + 1 or (x, y) in visited:
        return 0

    visited.add((x, y))

    if mp[x][y] == 9:
        return 1

    return sum(
        dfs(mp, visited, x + i, y + j, mp[x][y])
        for i, j in directions
        if 0 <= x + i < len(mp) and 0 <= y + j < len(mp[0])
    )


with open("input.txt") as f:
    mp = [[int(n) for n in list(l.strip("\n"))] for l in f.readlines()]

res = sum(dfs(mp, set(), x, y, -1) for x in range(len(mp)) for y in range(len(mp[0])))
print(res)
