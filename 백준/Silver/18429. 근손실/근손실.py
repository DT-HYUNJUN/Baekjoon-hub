def back():
    global cnt
    if len(res) == N:
        tmp = 0
        for i in res:
            tmp += lst[i]-K
            if tmp < 0:
                return
        else:
            cnt += 1
            return
        
    for i in range(N):
        if i not in res:
            res.append(i)
            back()
            res.pop()

N, K = map(int, input().split())
lst = [int(x) for x in input().split()]
res = []
cnt = 0
back()
print(cnt)