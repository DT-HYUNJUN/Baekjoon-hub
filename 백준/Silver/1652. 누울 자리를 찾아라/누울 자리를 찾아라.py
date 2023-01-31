N = int(input())
room = [[x for x in input()] for _ in range(N)]
cnt_r, cnt_c = 0, 0
space_r, space_c = 0, 0
for i in room:
    for j in i:
        if j == '.':
            cnt_r += 1
        else:
            if cnt_r > 1:
                space_r += 1
            cnt_r = 0
    if cnt_r > 1:
        space_r += 1
    cnt_r = 0
for i in range(N):
    for j in range(N):
        if room[j][i] == '.':
            cnt_c += 1
        else:
            if cnt_c > 1:
                space_c += 1
            cnt_c = 0
    if cnt_c > 1:
        space_c += 1
    cnt_c = 0
print(space_r, space_c)