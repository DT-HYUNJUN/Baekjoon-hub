N = int(input())
lst = [int(x) for x in input().split()]
set_list = sorted(list(set(lst)))
dic = {}
dic = {set_list[i] : i for i in range(len(set_list))}
for i in lst:
    print(dic[i], end=' ')