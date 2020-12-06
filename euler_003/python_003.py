#!/bin/python3

from math import sqrt, ceil
import sys

def largest_prime_factor(number):
    maxPrime = -1
    while number % 2 == 0:
        maxPrime = 2
        number //= 2

    for div in range(3, ceil(sqrt(n)) + 1, 2):
        while number % div == 0:
            number //= div
            maxPrime = div

    if number > 2:
        maxPrime = number

    return maxPrime


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime_factor(n))
