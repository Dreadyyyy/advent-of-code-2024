from functools import cache


@cache
def stones(value: int, turns_left: int) -> int:
    if turns_left == 0:
        return 1

    if value == 0:
        return stones(1, turns_left - 1)

    if (l := len(s := str(value))) % 2 == 0:
        return sum(stones(int(n), turns_left - 1) for n in (s[: l // 2], s[l // 2 :]))

    return stones(value * 2024, turns_left - 1)


with open("input.txt") as f:
    nums = [int(n) for n in f.read().strip("\n").split(" ")]

res = sum(stones(n, 75) for n in nums)
print(res)
