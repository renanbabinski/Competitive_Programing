t = int(input())

for i in range(t):
    n = input()
    k = len(n)
    n = int(n)
    p = int('1'*k)
    a = n//p + 9*(k-1)
    print(a)

