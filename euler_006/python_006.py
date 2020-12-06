def difference(n):
    sum_1 = (n * (n + 1) // 2) ** 2
    sum_2 = n*(n+1)*((2*n)+1)//6
    return sum_1 - sum_2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(difference(n))
