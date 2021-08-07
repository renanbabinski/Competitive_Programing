t = int(input())

for i in range(t):
    burles = int(input())
    c1 = burles // 3
    c2 = c1
    if burles % 3 == 1:
        c1 += 1
    if burles % 3 == 2:
        c2 += 1
    print("{} {}".format(c1, c2)) 