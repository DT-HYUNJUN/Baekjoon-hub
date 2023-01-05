N = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    status = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                status += 1
        if status == 0:
            cnt += 1
print(cnt)