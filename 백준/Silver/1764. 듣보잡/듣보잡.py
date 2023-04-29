N, M = map(int, input().split())
res = []
dic= {}
for i in range(N+M):
    name = input()
    dic[name] = dic.get(name, 0) + 1

for i in dic.keys():
    if dic[i] == 2:
        res.append(i)
print(len(res))
for i in sorted(res):
    print(i)