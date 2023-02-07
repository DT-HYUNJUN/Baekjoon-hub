delta = {
    'R' : ( 0,  1),
    'L' : ( 0, -1),
    'B' : ( 1,  0),
    'T' : (-1,  0),
    'RT': (-1,  1),
    'LT': (-1, -1),
    'RB': ( 1,  1),
    'LB': ( 1, -1),
}
k, s, move = input().split()
chess = [[0] * 8 for _ in range(8)]
kx, ky = 8 - int(k[1]), ord(k[0]) - 65
sx, sy = 8 - int(s[1]), ord(s[0]) - 65
chess[kx][ky] = 1
chess[sx][sy] = 2
for i in range(int(move)):
    cmd = input().strip()
    nkx = kx + delta[cmd][0]
    nky = ky + delta[cmd][1]
    nsx = sx + delta[cmd][0]
    nsy = sy + delta[cmd][1]
    if nkx <= -1 or nkx >= 8 or nky <= -1 or nky >= 8:
        continue
    else:
        if nkx == sx and nky == sy:
            if nsx <= -1 or nsx >= 8 or nsy <= -1 or nsy >= 8:
                continue
            else:
                chess[nsx][nsy] = 2
                chess[sx][sy] = 1
                chess[kx][ky] = 0
                kx, ky, sx, sy = nkx, nky, nsx, nsy
        else:
            chess[nkx][nky] = 1
            chess[kx][ky] = 0
            kx, ky= nkx, nky
for i in chess:
    if 1 in i:
        kx, ky = chess.index(i), i.index(1)
        break
for i in chess:
    if 2 in i:
        sx, sy = chess.index(i), i.index(2)
        break
k, s = chr(ky+65) + str(8-kx), chr(sy+65) + str(8-sx)
print(k)
print(s)