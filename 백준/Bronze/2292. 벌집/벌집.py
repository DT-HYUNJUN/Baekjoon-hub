N = int(input())
hive = cnt = 1
while hive < N:
    hive += cnt * 6
    cnt += 1
print(cnt)