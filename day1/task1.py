with open("input.txt", "r") as f:
    nums = [l.split("   ") for l in f.readlines()]

l1 = sorted([int(n) for n, _ in nums])
l2 = sorted([int(n) for _, n in nums])
res = sum(abs(n1 - n2) for n1, n2 in zip(l1, l2))
print(res)
