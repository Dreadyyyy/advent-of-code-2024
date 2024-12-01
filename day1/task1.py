with open("input.txt", "r") as f:
    l1, l2 = [], []
    for line in f.readlines():
        n1, n2 = [int(n) for n in line.split("   ")]
        l1.append(n1)
        l2.append(n2)

res = sum(abs(n1 - n2) for n1, n2 in zip(sorted(l1), sorted(l2)))
print(res)
