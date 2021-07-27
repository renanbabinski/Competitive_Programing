t = int(input())

for i in range(t):
    input() #blank line
    a = input().split(" ")
    b = input().split(" ")
    f = input().split(" ")
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    f = [int(i) for i in f]
    resposta = abs(a[0] - b[0]) + abs(a[1] - b[1])
    if (( a[0] == b[0] and a[0] == f[0] and min(a[1], b[1]) < f[1] and f[1] < max(a[1],b[1] )) 
    or  ( a[1] == b[1] and a[1] == f[1] and min(a[0], b[0]) < f[0] and f[0] < max(a[0],b[0]))):
        resposta += 2
    print(resposta)
