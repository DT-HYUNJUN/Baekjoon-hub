import sys
A = [[int(x) for x in sys.stdin.readline().split()] for _ in range(9)]
maximum = 0
index = 0
for i in range(9):    
    if maximum < max(A[i]):
        maximum = max(A[i])
        index = i
print(maximum)
print(index+1, A[index].index(maximum)+1)