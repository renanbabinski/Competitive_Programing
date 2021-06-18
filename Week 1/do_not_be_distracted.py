t = int(input())

letter_read = []

for i in range(t):
    order = None
    letter_read.clear()
    n = int(input())
    order = input() + '/'
    for j in range(n):
        if order[j] != order[j+1]:
            if order[j] in letter_read:
                print("NO")
                break
            else:
                letter_read.append(order[j])
        if j == (n-1):
            print("YES")