M = int(input())
N = int(input())
res = []
num = 1
while num ** 2 <= N:
    if M <= num ** 2 <= N:        
        res.append(num ** 2)
    num += 1
if res:
    print(sum(res))
    print(min(res))
else:
    print(-1)