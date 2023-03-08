n = int(input())
H = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
H_A = sorted([(H[i], A[i]) for i in range(n)], key=lambda x:x[1])
res = 0
for index, (tree, grow) in enumerate(H_A):
    res += tree + (grow * (index))
print(res)