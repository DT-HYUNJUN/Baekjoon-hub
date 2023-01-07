T = int(input())
for _ in range(T):
    lst = list(input().split())
    num = float(lst[0])
    for i in lst:
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        elif i == '#':
            num -= 7
    print("%0.2f" % num)   