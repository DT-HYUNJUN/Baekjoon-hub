S = list(input())
dic = {chr(c): 0 for c in range(97, 97+26)}
for c in S:
    dic[c] = dic.get(c, 0) + 1
for k, v in dic.items():
    print(dic[k], end=' ')