from functools import cache
from math import inf


@cache
def min_tokens(
    a: tuple[int, int], b: tuple[int, int], goal: tuple[int, int]
) -> int | None:
    if goal == (0, 0):
        return 0

    if goal[0] < 0 or goal[1] < 0:
        return None

    opts = [
        min_tokens(a, b, (goal[0] - a[0], goal[1] - a[1])),
        min_tokens(a, b, (goal[0] - b[0], goal[1] - b[1])),
    ]
    opts = [inf if o is None else o for o in opts]
    opts[0] += 3
    opts[1] += 1

    return None if (mn := min(opts)) == inf else int(mn)


with open("input.txt") as f:
    blocks = f.read().split("\n\n")

button_a = [b.split("\n")[0] for b in blocks]
button_a = [l.split(" ")[2:] for l in button_a]
button_a = [(int(x[1:-1]), int(y[1:])) for x, y in button_a]

button_b = [b.split("\n")[1] for b in blocks]
button_b = [l.split(" ")[2:] for l in button_b]
button_b = [(int(x[1:-1]), int(y[1:])) for x, y in button_b]

coords = [b.split("\n")[2] for b in blocks]
coords = [l.split(" ")[1:] for l in coords]
coords = [(int(x[2:-1]), int(y[2:])) for x, y in coords]

res = [min_tokens(a, b, c) for a, b, c in zip(button_a, button_b, coords)]
print(len(res))
print(len([t for t in res if t is not None]))
res = sum(t for t in res if t is not None)
print(res)
