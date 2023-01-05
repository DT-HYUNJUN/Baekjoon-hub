A = int(input())
B = int(input())
C = int(input())
lst = list(str(A*B*C))
cnt = [0] * 10

for num in lst:
    cnt[int(num)] += 1

for i in cnt:
    print(i)     