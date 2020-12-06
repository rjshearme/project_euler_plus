import math

T = int(input())

for _ in range(T):
    n = int(input())
    factorial_n = math.factorial(n)
    integers_in_factorial_n = map(int, str(factorial_n))
    print(sum(integers_in_factorial_n))

