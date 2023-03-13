P, K = map(int, input().split())

is_bad = True
for i in range(2, K):
    if P % i == 0:
        print('BAD', i)
        is_bad = False
        break
if is_bad:
    print('GOOD')