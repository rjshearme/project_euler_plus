from math import factorial as f

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    output = f(N+M) // f(N) // f(M) % (1000000007)
    print((output))
