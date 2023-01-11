N = int(input())
sum = 0
while N>0:
    head = N % 10
    N //= 10
    sum += head
print(sum)