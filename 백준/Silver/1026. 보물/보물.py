N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
total = 0
for i in range(N):
    total += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
print(total)