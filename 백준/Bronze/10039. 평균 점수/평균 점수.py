sum = 0
for _ in range(5):
    num = int(input())
    if num < 40:
        sum += 40
    else:
        sum += num
print(sum//5)