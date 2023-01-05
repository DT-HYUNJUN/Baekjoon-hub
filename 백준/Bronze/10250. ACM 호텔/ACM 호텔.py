T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N // H + 1
    room = N % H
    if N % H == 0:
        floor = N // H
        room = H
    print(f'{room*100+floor}')