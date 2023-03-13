E, S, M = map(int, input().split())
cnt = 0
e = 1
s = 1
m = 1
while True:
    cnt += 1
    if e == E and s == S and m == M:
        print(cnt)
        break

    e += 1
    s += 1
    m += 1

    if e > 15:
        e //= 15
    if s > 28:
        s //= 28
    if m > 19:
        m //= 19