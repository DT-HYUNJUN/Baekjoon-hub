lst = []
for _ in range(int(input())):
    name, day, month, year = input().split()
    day ,month ,year = map(int,(day, month, year))
    lst.append((year, month, day, name))
lst.sort()
print(lst[-1][3])
print(lst[0][3])