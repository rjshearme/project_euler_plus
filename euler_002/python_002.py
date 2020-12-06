t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fib_1, fib_2, result = 1, 2, 2
    while fib_2 + fib_1 < n:
        fib_temp = fib_1 + fib_2
        if fib_temp % 2 == 0:
            result += fib_temp
        fib_1 = fib_2
        fib_2 = fib_temp
    print(result)
