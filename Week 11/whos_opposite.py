t = int(input())

for i in range(t):
    a, b, c = input().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    d = 0
    circle_lenght = abs(a-b)*2
    if a <= circle_lenght and b <= circle_lenght and c <= circle_lenght:
        if c > (circle_lenght // 2):
            d = c - (circle_lenght // 2)
        else:
            d = c + (circle_lenght // 2)
    else:
        d = -1

    print(d)