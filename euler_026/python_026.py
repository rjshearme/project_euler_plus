def get_len_cycle(d):
    if d % 2 == 0 or d % 5 == 0 or d <= 1:
        return 0
    n = 1
    while not pow(10, n, d) == 1 % d:
        n += 1
    return n

def get_max_len_cycle(limit):
    return max(get_len_cycle(d) for d in range(limit))

len_cycle_for_d = {d: get_len_cycle(d) for d in range(10_000)}

T = int(input())

for _ in range(T):
    n = int(input())
    print(max((d for d in len_cycle_for_d if d < n), key=lambda x: len_cycle_for_d[x]))