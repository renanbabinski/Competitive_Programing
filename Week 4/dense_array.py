t = int(input())

for i in range(t):
    n = int(input())
    a = []
    a = input().split(' ')
    numbers_needed = 0
    previous = 0
    next = previous + 1
    for j in range(n-1):
        if (int(max(a[previous:next+1])) / int(min(a[previous:next+1]))) > 2:
            numbers_needed += 1
            previous_list = a[:previous+1]
            next_list = a[next:]
            previous_list.append(2*int(min(a[previous:next+1]))) #adiciona um elemento na lista com o dobro do menor valor
            a = previous_list + next_list
            previous += 1
            next += 1
        print("----")
        print(a)
        print(a[previous:next+1] + a[previous:next+1])
        print("----")
        print(max(a[previous:next+1]), min(a[previous:next+1]))
        previous += 1
        next += 1
        
    print(numbers_needed)