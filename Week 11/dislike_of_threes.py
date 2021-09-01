t = int(input())
numbers = []
j = 0
while len(numbers) <= 1000:
    j += 1
    if j % 3 == 0 or j % 10 == 3:
        continue
    numbers.append(int(j))
    

for i in range(t):
    k = int(input())
    print(numbers[k - 1])