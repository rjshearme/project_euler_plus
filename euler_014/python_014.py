CACHE_LIMIT = 5_000_000


def memo(f):
    f.cache = [0] * (CACHE_LIMIT + 1)
    f.cache[1] = 1

    def _f(n):
        cache_val = 0
        if n < CACHE_LIMIT:
            cache_val = f.cache[n]
        func_val = cache_val if cache_val else f(n)
        if not cache_val and n < CACHE_LIMIT:
            f.cache[n] = func_val
        return func_val
    return _f


@memo
def collatz(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + collatz(n // 2)
    if n % 2 == 1:
        return 1 + collatz(3 * n + 1)

max_values = [0] * (CACHE_LIMIT + 1)
max_seen = 1
keep_i = 1
for i in range(1, CACHE_LIMIT+1):
    collatz_i = collatz(i)
    if collatz_i >= max_seen:
        keep_i = i
        max_seen = collatz_i
    max_values[i] = keep_i

T = int(input("T "))
for _ in range(T):
    n = int(input())
    print(max_values[n])