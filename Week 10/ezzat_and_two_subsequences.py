t = int(input())

for i in range(t):
    n = int(input())
    array = []
    array = input().split(' ')
    array = [int(j) for j in array]
    maximo = max(array)
    array.pop(array.index(maximo))
    avg1 = maximo
    soma = sum(array)
    avg2 = soma/(len(array))
    result = avg1 + avg2
    print(result)
