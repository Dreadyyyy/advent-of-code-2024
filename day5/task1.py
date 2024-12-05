def check(rules: dict[int, list[int]], update: list[int]) -> bool:
    prev = set()
    for n in update:
        if any(p in prev for p in rules.get(n, [])):
            return False
        prev.add(n)
    return True


with open("input.txt") as f:
    rules = {}
    while (l := f.readline()) != "\n":
        n1, n2 = map(int, l.split("|"))
        rules.setdefault(n1, [])
        rules[n1].append(n2)

    updates = [list(map(int, l.split(","))) for l in f.readlines()]


updates = [u for u in updates if check(rules, u)]

res = sum(u[len(u) // 2] for u in updates)
print(res)
