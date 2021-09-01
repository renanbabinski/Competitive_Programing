t = int(input())
x = 0
y = 0

def ceil(k):
    k = int(k + (0 if k == int(k) else 1))
    return k

for i in range(t):
    k = int(input())
    root = ceil(pow(k, 1/2))
    #print(root)
    max_value = root**2
    min_value = (root-1)**2 + 1
    if abs(k-max_value) < root:
        x = root
        y = abs(k-max_value) + 1
    else:
        y = root
        x = abs(k-min_value) + 1
    
    print("{} {}".format(x, y))
    