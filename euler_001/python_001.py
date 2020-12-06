def solution(n):
    of3 = (n-1) // 3
    of5 = (n-1) // 5
    of15 = (n-1) // 15
    return (
        3 * of3 * (of3+1)
        + 5 * of5 * (of5+1)
        - 15 * of15 * (of15+1)
    ) // 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solution(n))
