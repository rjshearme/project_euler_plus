T = int(input())

def gen_fibs(limit):
    fibs = [1, 1]
    max_len_seen = 1
    fib_len_dict = {
        1: 1
    }
    fib_term = 2
    len_last_fib = 1
    while len_last_fib < limit:
        fibs.append(fibs[-2] + fibs[-1])
        fib_term += 1
        len_last_fib =  len(str(fibs[-1]))
        if len_last_fib > max_len_seen:
            fib_len_dict[len_last_fib] = fib_term
            max_len_seen = len_last_fib
    return fib_len_dict


fibs_up_to_len_5000 = gen_fibs(5000)


for _ in range(T):
    n = int(input())
    print(fibs_up_to_len_5000[n])