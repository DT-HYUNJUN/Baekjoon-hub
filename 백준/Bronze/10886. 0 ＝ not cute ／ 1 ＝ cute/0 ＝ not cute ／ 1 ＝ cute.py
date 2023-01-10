N = int(input())
sum = 0
for i in range(N):
    V = int(input())
    sum += V
if float(sum) < N/2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')