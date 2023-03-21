
N = int(input())
W = [int(x) for x in input().split()]
res = 0
def back(energy):
    global res
    if len(W) == 2:
        res = max(res, energy)
        return
    for i in range(1, len(W)-1):
        tmp = W[i-1] * W[i+1]
        index = W.pop(i)
        back(tmp + energy)
        W.insert(i, index)
back(0)

print(res)
