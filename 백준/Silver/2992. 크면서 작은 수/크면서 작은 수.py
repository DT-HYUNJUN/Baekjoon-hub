num = int(input())
lst = sorted([int(x) for x in str(num)])
N = len(lst)
res = []
ans = []
def back():
    if len(res) == N:
        tmp = [str(lst[i]) for i in res]
        tmp_num = int(''.join(tmp))
        if tmp_num > num:
            ans.append(tmp_num)
        return
    
    for i in range(N):
        if i not in res:
            res.append(i)
            back()
            res.pop()
back()
if ans:
    print(ans[0])
else:
    print(0)