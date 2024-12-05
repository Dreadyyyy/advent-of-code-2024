from functools import cmp_to_key


def check(rules: dict[int, list[int]], update: list[int]) -> bool:
    prev = set()
    for n in update:
        if any(p in prev for p in rules.get(n, [])):
            return False
        prev.add(n)
    return True


with open("input.txt") as f:
    rules, cmp = {}, {}
    while (l := f.readline()) != "\n":
        n1, n2 = map(int, l.split("|"))
        rules.setdefault(n1, [])
        rules[n1].append(n2)
        cmp[(n1, n2)] = -1
        cmp[(n2, n1)] = 1

    updates = [list(map(int, l.split(","))) for l in f.readlines()]

updates = [
    sorted(u, key=cmp_to_key(lambda x, y: cmp.get((x, y), x - y)))
    for u in updates
    if not check(rules, u)
]

res = sum(u[len(u) // 2] for u in updates)
print(res)
