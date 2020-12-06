from string import ascii_uppercase as letters

N = int(input())
names = []

for _ in range(N):
    names.append(input())

names = sorted(names)

Q = int(input())
for _ in range(Q):
    search_name = input()
    pos_value = names.index(search_name) + 1
    name_val = sum([letters.index(i) + 1 for i in search_name])
    print(name_val * pos_value)
