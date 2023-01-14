L = int(input())
string = input()
res = 0
r, M = 31, 1234567891
for i in range(L):
    res += (ord(string[i])-96)*(r**i)
print(res % M)