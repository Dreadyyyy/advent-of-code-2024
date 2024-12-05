from functools import cmp_to_key


with open("input.txt") as f:
    cmp = {}
    while (l := f.readline()) != "\n":
        n1, n2 = map(int, l.split("|"))
        cmp[(n1, n2)] = -1
        cmp[(n2, n1)] = 1

    updates = [list(map(int, l.split(","))) for l in f.readlines()]

key = cmp_to_key(lambda x, y: cmp[(x, y)])
updates = [su for u in updates if u != (su := sorted(u, key=key))]

res = sum(u[len(u) // 2] for u in updates)
print(res)
