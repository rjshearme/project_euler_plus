def zellers_congruence(year, month, day):
    if month <= 2:
        month += 12
        year -= 1
    zero_based_century, year_of_the_century = divmod(year, 100)
    return (day + (13*(month+1) // 5) + year_of_the_century + (year_of_the_century // 4) + (zero_based_century // 4) - (2 * zero_based_century)) % 7

def get_date_generator(y1, m1, d1, y2, m2, d2):
    next_year, next_month, next_day = (y1, m1, d1) if d1 == 1 else (y1, m1+1, 1) if m1 < 12 else (y1+1, 1, 1)
    while next_year < y2 or (next_year==y2 and next_month<m2) or (next_year==y2 and next_month==m2 and next_day<=d2):
        yield next_year, next_month, next_day
        next_year, next_month, next_day = (next_year, next_month+1, 1) if next_month < 12 else (next_year+1, 1, 1)


T = int(input())
for _ in range(T):
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())
    day_gen = get_date_generator(y1, m1, d1, y2, m2, d2)
    print(sum(1 for year, month, day in day_gen if zellers_congruence(year, month, day) == 1))