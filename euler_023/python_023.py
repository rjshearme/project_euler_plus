import math

T = int(input())


def d(number):
    div_sum = 1
    for divisor in range(2, math.ceil(math.sqrt(number))):
        if number % divisor == 0:
            div_sum += divisor + number // divisor

    return div_sum


def gen_abundant_numbers(limit):
    abundant_numbers = set()
    for i in range(1, limit + 1):
        sum_proper_divisors = d(i)
        if sum_proper_divisors > i:
            abundant_numbers.add(i)
    return abundant_numbers


abundant_numbers = gen_abundant_numbers(28123 - 12)

sorted_abundant_numbers = sorted(abundant_numbers)
for _ in range(T):
    n = int(input())
    output = "NO"
    if n > 28123:
        output = "YES"

    else:
        for abundant_number in sorted_abundant_numbers:
            if abundant_number >= n:
                output = "NO"
                break
            if n - abundant_number in abundant_numbers:
                output = "YES"
                break
    print(output)
