t = int(input())

for i in range(t):
    n = int(input())
    lista = list(input())
    if 'R' in lista:
        start = lista.index('R')
    elif 'B' in lista:
        start = lista.index('B')
    else:
        start = 0
    head = start - 1
    tail = start + 1
    while '?' in lista:
        if start == 0 and lista[0] == '?':
            lista[start] = 'B'
        if head >= 0:
            if lista[head] == '?' and lista[head+1] == 'R':
                lista[head] = 'B'
            elif lista[head] == '?' and lista[head+1] == 'B':
                lista[head] = 'R'
            head = head - 1
        if tail < len(lista):
            if lista[tail] == '?' and lista[tail-1] == 'R':
                lista[tail] = 'B'
            elif lista[tail] == '?' and lista[tail-1] == 'B':
                lista[tail] = 'R'
            tail = tail + 1

    string=''.join([str(item) for item in lista])
    print(string)