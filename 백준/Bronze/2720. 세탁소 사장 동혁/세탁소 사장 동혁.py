T = int(input())
quarter, dime, nickel, penny = 25, 10, 5, 1
for _ in range(T):
    C = int(input())
    cnt = [0, 0, 0, 0]
    while C != 0:
        if (C // quarter) > 0:
            C -= 25
            cnt[0] += 1
        elif (C // dime) > 0:
            C -= 10
            cnt[1] += 1
        elif (C // nickel) > 0:
            C -= 5
            cnt[2] += 1
        elif (C // penny) > 0:
            C -= 1
            cnt[3] += 1
    print(*cnt)