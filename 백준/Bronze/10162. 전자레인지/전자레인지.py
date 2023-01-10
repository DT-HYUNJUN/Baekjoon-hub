T = int(input())
time = [300, 60, 10]
res = []

if T % 10 != 0:
    print(-1)
else:
    for i in time:
        count = T // i
        res.append(count)
        T %= i
    print(res[0], res[1], res[2])