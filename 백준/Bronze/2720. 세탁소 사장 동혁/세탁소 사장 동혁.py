T = int(input())
for _ in range(T):
    C = int(input())
    lst = [25, 10, 5, 1]
    cnt = []
    for i in lst:
        cnt.append(C // i)
        C %= i
    print(*cnt)