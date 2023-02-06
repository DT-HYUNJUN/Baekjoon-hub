N = int(input())
lst_1 = [int(x) for x in input().split()]
M = int(input())
lst_2 = [int(x) for x in input().split()]
dic = {}
for i in lst_1:
    dic[i] = dic.get(i, 0) + 1
for i in lst_2:
    if i in dic:
        print(1)
    else:
        print(0)