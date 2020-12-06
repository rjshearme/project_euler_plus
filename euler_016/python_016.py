for _ in range(t):
    n = int(input())
    digits = sum(list(map(int, list(str(2**n)))))
    print(digits)