def is_palindromic(number):
    str_number = str(number)
    return str_number == str_number[::-1]

def get_palindromic_numbers_set():
    palindromic_set = set()
    for i in range(999, 1, -1):
        for j in range(999, 1, -1):
            number = i * j
            if is_palindromic(number):
                palindromic_set.add(number)
    return palindromic_set

def get_max_palindrome_less_than(limit):
    return max(pal for pal in palindromic_set if pal < limit)


palindromic_set = get_palindromic_numbers_set()

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(get_max_palindrome_less_than(n))
