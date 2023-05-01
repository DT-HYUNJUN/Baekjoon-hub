N = int(input())
cnt = 0
car_in = {}
car_out = []
for i in range(N):
    car = input()
    car_in[car] = i
for i in range(N):
    car = input()
    car_out.append(car)

for i in range(N):
    for j in range(i+1, N):
        if car_in[car_out[i]] > car_in[car_out[j]]:
            cnt += 1
            break
print(cnt)