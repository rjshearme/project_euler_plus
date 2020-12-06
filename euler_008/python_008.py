#!/bin/python3
from operator import mul
from functools import reduce
import sys

def max_product(num, k):
    products = set()
    numbers = [int(x) for x in num]
    for i in range(0, n-k):
        products.add(reduce(mul, numbers[i:i+k], 1))
    return max(products)


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(max_product(num, k))
