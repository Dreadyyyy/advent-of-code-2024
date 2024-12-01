with open("input.txt") as f:
    l1, l2 = [], []
    for line in f.readlines():
        n1, n2 = [int(n) for n in line.split("   ")]
        l1.append(n1)
        l2.append(n2)

m1, m2 = {}, {}
for n in l1:
    m1[n] = m1.setdefault(n, 0)
    m1[n] += 1
for n in l2:
    m2[n] = m2.setdefault(n, 0)
    m2[n] += 1

res = 0
for k in m1.keys():
    res += k * m1[k] * m2.setdefault(k, 0)

print(res)
