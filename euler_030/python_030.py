def sum_eq_str(number, power):
    return number == sum(map(lambda n: pow(int(n), power), str(number)))

Nth_power = int(input())
total = 0

for i in range(10, 1_000_000):
    if sum_eq_str(i, Nth_power):
        total += i

print(total)
