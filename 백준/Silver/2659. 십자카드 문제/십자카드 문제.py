lst = [int(x) for x in input().split()]
cnt = 1
def find(lst):
    tmp = ''
    min_num = int(''.join(map(str, lst)))
    for i in range(4):
        for j in range(i, (i+4)):
            tmp += str(lst[j%4])
        if min_num > int(tmp):
            min_num = int(tmp)
        tmp = ''
    return min_num

for i in range(1111, find(lst)):
    if '0' in str(i) or i != find(list(str(i))):
        continue
    cnt += 1
print(cnt)