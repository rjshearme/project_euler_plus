import math

def quadratic(n, a, b):
    return n**2 + a * n + b

def is_prime(x):
    if x <= 1 or x % 2 == 0:
        return False
    for divisor in range(3, math.floor(math.sqrt(x)) + 1, 2):
        if x % divisor == 0:
            return False
    return True

def is_prime_quadratic(n, a, b):
    if n == 1 and a %2 == 1:
        return True
    quad_val = quadratic(n, a, b)
    return is_prime(quad_val)

def max_consecutive_primes(a, b):
    n = 0
    if not is_prime(b):
        return 0
    while is_prime_quadratic(n, a, b):
        n += 1
    return n

N = int(input())

max_found = A = B = 0
for b in range(1, N):
    for a in range(-N, 0):
        length_prime_sequence = max_consecutive_primes(a, b)
        if length_prime_sequence > max_found:
            A, B, max_found = a, b, length_prime_sequence

print(A, B)