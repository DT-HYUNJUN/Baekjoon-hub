import sys
lst = []
res = []
for _ in range(28):
    num = int(sys.stdin.readline())
    lst.append(num)
for i in range(1, 31):
    if i not in lst:
        res.append(i)
res.sort()
for j in res:
    print(j)