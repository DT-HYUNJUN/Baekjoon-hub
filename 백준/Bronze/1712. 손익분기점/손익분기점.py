A, B, C = map(int, input().split())
if C <= B:
    print(-1)
else:
    n = A/(C-B)
    n += 1
    print(int(n))