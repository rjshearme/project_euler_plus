import functools
import math
from collections import defaultdict

prime_limit = 1_000_000

def sieve_of_eratosthenes(limit):
    sieve_array = [True] * (limit + 1)
    sieve_array[0] = sieve_array[1] = False
    for index, is_prime in enumerate(sieve_array):
        if not is_prime:
            continue
        for multiple_index in range(index*2, limit+1, index):
            sieve_array[multiple_index] = False
        sieve_array[index] = index
    return sieve_array

primes = [prime for prime in sieve_of_eratosthenes(prime_limit) if prime]

def fast_count_divisors(n):
    i = 0
    divisors = 1
    while primes[i] <= n:
        p = primes[i]
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        if count > 0:
            divisors *= count + 1
        i += 1
    return divisors


def triangular_number_generator():
    i = 0
    total = 0
    while True:
        i += 1
        total += i
        yield total


DIVISOR_LIMIT = 1000


triangular_number_divisor_lookup = {}
triangular_numbers = triangular_number_generator()
triangular_number = next(triangular_numbers)
num_div_tri_num = fast_count_divisors(triangular_number)

for number_of_divisors in range(1, DIVISOR_LIMIT + 1):
    while num_div_tri_num <= number_of_divisors:
        triangular_number = next(triangular_numbers)
        num_div_tri_num = fast_count_divisors(triangular_number)
    triangular_number_divisor_lookup[number_of_divisors] = triangular_number


T = int(input())
for _ in range(T):
    n = int(input())
    print(triangular_number_divisor_lookup[n])
