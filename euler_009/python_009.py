#!/bin/python3


def find_triples(n):
    max_prod = -1
    for a in range(3, (N//3) + 1):
        b = (N*N - 2*N*a) // (2*N - 2*a)
        c = N - b - a
        if a*a + b*b == c*c:
            max_prod = max(max_prod, a * b * c)
    return max_prod


T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(find_triples(N))
