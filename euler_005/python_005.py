from collections import defaultdict


def get_LCM(n_arr, factors=None, last_pri=2):
    factors = defaultdict(int) if factors is None else factors
    if len(n_arr) == sum(n_arr):
        total = 1
        for prime, exponent in factors.items():
            total *= prime ** exponent
        return total

    elif any([n % last_pri == 0 for n in n_arr]):
        n_arr = [n // last_pri if n % last_pri == 0 else n for n in n_arr]
        factors[last_pri] += 1
        return get_LCM(n_arr, factors, last_pri)

    else:
        return get_LCM(n_arr, factors, last_pri + 1)


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(get_LCM(range(1, n + 1)))




