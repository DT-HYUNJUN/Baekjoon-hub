n = int(input())
dic = {}
for i in range(n):
    name, log = map(str, input().split())
    dic[name] = log
print(*sorted([k for k, v in dic.items() if v == 'enter'], reverse=True), sep='\n')