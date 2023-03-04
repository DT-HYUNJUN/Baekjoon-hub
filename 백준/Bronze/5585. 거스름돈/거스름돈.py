N = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
change = 0
for i in coin:
    change += int(N/i)
    N %= i
print(change)