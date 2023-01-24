N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
cnt_list = [1] * N
for i in range(N):
    cnt = 0
    weight = lst[i][0]
    height = lst[i][1]
    for j in range(N):
        if weight < lst[j][0] and height < lst[j][1]:
            cnt += 1
    cnt_list[i] += cnt
print(*cnt_list)