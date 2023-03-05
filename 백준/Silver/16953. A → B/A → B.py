A, B = map(int, input().split())
cnt = 0
while True:
    cnt += 1
    if A == B:
        print(cnt)
        break
    tmp = B
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    if tmp == B:
        print(-1)
        break