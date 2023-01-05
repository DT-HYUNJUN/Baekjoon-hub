M = int(input())
N = int(input())
cnt = 0
prime = []
for i in range(M, N+1):
    status = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                status += 1
        if status == 0:
            prime.append(i)
if sum(prime) > 0:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)