def check(nums: list[int], i: int, curr: int, n: int) -> bool:
    if i == len(nums):
        return curr == n

    return any(
        check(nums, i + 1, r, n) for r in (curr + nums[i], curr * nums[i]) if r <= n
    )


with open("input.txt") as f:
    entries = [l.split(":") for l in f.readlines()]

entries = [(int(n), l.strip(" \n")) for n, l in entries]
entries = [(n, list(map(int, l.split(" ")))) for n, l in entries]

res = sum(n for n, nums in entries if check(nums, 1, nums[0], n))
print(res)
