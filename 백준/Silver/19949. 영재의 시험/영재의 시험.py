answer = [int(x) for x in input().split()]
yj = []
ans = 0
def back(depth):
    global ans
    if depth == 10:
        cnt = 0
        for i in range(10):
            if answer[i] == yj[i]:
                cnt +=1
        if cnt >= 5:
            ans += 1
        return
    for i in range(1, 6):
        if depth > 1 and yj[depth-2] == yj[depth-1] == i:
            continue
        yj.append(i)
        back(depth+1)
        yj.pop()        
back(0)
print(ans)