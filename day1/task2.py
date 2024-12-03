with open("input.txt", "r") as f:
    nums = [l.split("   ") for l in f.readlines()]

l1 = [int(n) for n, _ in nums]
l2 = [int(n) for _, n in nums]

m1, m2 = {}, {}
for n in l1:
    m1[n] = m1.get(n, 0) + 1
for n in l2:
    m2[n] = m2.get(n, 0) + 1

res = sum(k * m1[k] * m2.get(k, 0) for k in m1.keys())
print(res)
