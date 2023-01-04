A, B = map(str, input().split())
A_temp = [0, 0, 0]
B_temp = [0, 0, 0]
for i in range(3):
    A_temp[-i-1] = A[i]
for i in range(3):
    B_temp[-i-1] = B[i]
A = A_temp
B = B_temp
res = max(A,B)
for i in res:
    print(i,end='')