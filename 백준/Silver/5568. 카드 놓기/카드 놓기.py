from itertools import permutations as pm
n = int(input())
k = int(input())
lst = [input() for _ in range(n)]
dic = {}
for i in pm(lst, k):
    num = ''.join(i)
    dic[num] = dic.get(num, 0) + 1
print(len(dic))