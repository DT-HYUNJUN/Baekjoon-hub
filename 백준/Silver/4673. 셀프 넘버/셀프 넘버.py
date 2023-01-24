def d(n):
    n = n + sum(map(int, str(n)))
    return n

no_self_num = []

for i in range(1, 10001):
    no_self_num.append(d(i))

for i in range(1, 10001):
    if i not in no_self_num:
        print(i)