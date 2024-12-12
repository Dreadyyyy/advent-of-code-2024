def area(
    mp: list[str], visited: set[tuple[int, int]], curr: str, x: int, y: int
) -> int:
    if not 0 <= x < len(mp) or not 0 <= y < len(mp[0]) or mp[x][y] != curr:
        return 0

    if (x, y) in visited:
        return 0

    visited.add((x, y))
    return 1 + sum(
        area(mp, visited, curr, x + i, y + j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if (i ^ j) and (not i or not j)
    )


def in_bounds(mp: list[str], x: int, y: int, curr: str) -> bool:
    return 0 <= x < len(mp) and 0 <= y < len(mp[0]) and mp[x][y] == curr


def add_edge(
    mp: list[str],
    edges: set[tuple[int, int, int, int]],
    x_prev: int,
    y_prev: int,
    x_curr: int,
    y_curr: int,
) -> None:
    i, j = x_prev - x_curr, y_prev - y_curr
    i, j = not i, not j

    xl, yl = x_prev, y_prev
    xr, yr = x_curr, y_curr
    while in_bounds(mp, xl, yl, mp[x_prev][y_prev]) and not in_bounds(
        mp, xr, yr, mp[x_prev][y_prev]
    ):
        edges.add((xl, yl, xr, yr))
        xl += i
        yl += j
        xr += i
        yr += j

    xl, yl = x_prev, y_prev
    xr, yr = x_curr, y_curr
    while in_bounds(mp, xl, yl, mp[x_prev][y_prev]) and not in_bounds(
        mp, xr, yr, mp[x_prev][y_prev]
    ):
        edges.add((xl, yl, xr, yr))
        xl -= i
        yl -= j
        xr -= i
        yr -= j


def sides(
    mp: list[str],
    visited: set[tuple[int, int]],
    edges: set[tuple[int, int, int, int]],
    curr: str,
    x_prev: int,
    y_prev: int,
    x_curr: int,
    y_curr: int,
) -> int:
    if (x_prev, y_prev, x_curr, y_curr) in edges:
        return 0

    if (
        not 0 <= x_curr < len(mp)
        or not 0 <= y_curr < len(mp[0])
        or mp[x_curr][y_curr] != curr
    ):
        add_edge(mp, edges, x_prev, y_prev, x_curr, y_curr)
        return 1

    if (x_curr, y_curr) in visited:
        return 0

    visited.add((x_curr, y_curr))

    return sum(
        sides(mp, visited, edges, curr, x_curr, y_curr, x_curr + i, y_curr + j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if (i ^ j) and (not i or not j)
    )


with open("input.txt") as f:
    mp = [l.strip("\n") for l in f.readlines()]

visited_a, visited_s = set(), set()
res = sum(
    area(mp, visited_a, mp[x][y], x, y)
    * sides(mp, visited_s, set(), mp[x][y], -1, -1, x, y)
    for x in range(len(mp))
    for y in range(len(mp[0]))
)
print(res)
