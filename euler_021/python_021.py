import math
T = int(input())

def d(number):
    div_sum = 1
    for divisor in range(2, math.floor(math.sqrt(number))):
        if number % divisor == 0:
            div_sum += divisor + number // divisor

    return div_sum

def gen_amicable_numbers(limit):
    seen = set()
    amicable_numbers = set()
    for i in range(limit+1):
        if i in seen:
            continue
        d_of_i = d(i)
        d_of_d_of_i = d(d_of_i)
        if i == d_of_d_of_i and i != d_of_i:
            amicable_numbers ^= {i, d_of_i}
            seen.add(d_of_i)
    return amicable_numbers

amicable_numbers = gen_amicable_numbers(100_000)

for _ in range(T):
    n = int(input())
    print(sum(amicable_number for amicable_number in amicable_numbers  if amicable_number < n))
