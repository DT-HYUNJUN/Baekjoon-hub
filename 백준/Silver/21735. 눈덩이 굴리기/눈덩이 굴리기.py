N, M = map(int, input().split())
lst = [0] + [int(x) for x in input().split()]

res = 0

def back(index, total, time):
    global res
    if time > M:
        return

    if time <= M:
        res = max(res, total)

    if index <= N-1:
        back(index+1, total+lst[index+1], time +1)
    if index <= N-2:
        back(index+2, total//2+lst[index+2], time +1)

back(0, 1, 0)
print(res)