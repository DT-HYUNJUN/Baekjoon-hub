A = int(input())
B = int(input())
C = int(input())
lst = list(str(A*B*C))
for i in range(10):
    print(lst.count(str(i)))