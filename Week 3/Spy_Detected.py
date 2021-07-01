t = int(input())

for i in range(t):
    n = int(input())
    numbers = None
    conjunto = None
    numbers = input().split(' ')
    conjunto = set(numbers)
    conjunto = list(conjunto)
    if(numbers.count(conjunto[0]) == 1):
        print(numbers.index(conjunto[0])+1)
    else:
        print(numbers.index(conjunto[1])+1)