import numpy as np

t = int(input())

def append_array(array, x):
    array = np.hstack((array, x))
    return array

for i in range(t):
    n = int(input())
    array = np.full((n,n), '.')
    for j in range(n):
        linha = list(input())
        linha = np.array(linha)
        array[j] = linha
    mask = array == "*"
    indice_x, indice_y = np.nonzero(mask)
    if indice_x[0] == indice_x[1]:
        indice_y = append_array(indice_y, indice_y)
        if indice_x[0] == 0:
            indice_x = append_array(indice_x, indice_x + 1)
        elif indice_x[0] == n-1:
            indice_x = append_array(indice_x, indice_x - 1)
        else:
            indice_x = append_array(indice_x, indice_x + 1)
    elif indice_y[0] == indice_y[1]:
        indice_x = append_array(indice_x, indice_x)
        if indice_y[0] == 0:
            indice_y = append_array(indice_y, indice_y + 1)
        elif indice_y[0] == n-1:
            indice_y = append_array(indice_y, indice_y - 1)
        else:
            indice_y = append_array(indice_y, indice_y + 1)
    else:
        indice_x = append_array(indice_x, indice_x)
        indice_y = append_array(indice_y, indice_y[1])
        indice_y = append_array(indice_y, indice_y[0])
    
    array[indice_x, indice_y] = '*'
    
    for i in range(n):
        for j in range(n):
            print(array[i][j], end='')
        print()
    