from string import ascii_letters, digits


def is_antinode(mp: list[str], x: int, y: int) -> bool:
    dist = {c: set() for c in ascii_letters + digits}
    for i, s in enumerate(mp):
        for j, c in enumerate(s):
            if c == ".":
                continue

            di, dj = i - x, j - y
            if (
                (x + 2 * di, y + 2 * dj) in dist[c]
                or di % 2 == 0
                and dj % 2 == 0
                and (x + di // 2, y + dj // 2) in dist[c]
            ):
                return True
            dist[c].add((i, j))

    return False


with open("input.txt") as f:
    mp = [s.strip("\n") for s in f.readlines()]

res = sum(is_antinode(mp, x, y) for x in range(len(mp)) for y in range(len(mp[0])))
print(res)
