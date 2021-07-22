def get_float(value):
    value = value.replace("$", "")
    value = value.replace(".", "")
    value = int(value)
    return value

n = int(input())
initial_balance = get_float(input())
late_to_work = 0

for days in range(n):
    initial_balance += get_float(input())
    if initial_balance % 100 != 0:
        late_to_work += 1

print(late_to_work)

