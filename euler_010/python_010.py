import math
import itertools

T = int(input())

prime_limit = 10**6

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

prime_sieve = sieve_of_eratosthenes(prime_limit)
prime_sieve_cumulative_sum = list(itertools.accumulate(prime_sieve))

for _ in range(T):
    n = int(input())
    print(prime_sieve_cumulative_sum[n])