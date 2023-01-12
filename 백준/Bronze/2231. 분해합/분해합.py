N = int(input())
Sum = 0
A = []
for i in range(1, N+1):
    tmp = list(map(int, str(i)))
    Sum = i + sum(tmp)
    if Sum == N:
        print(i)
        break
else:
    print(0)