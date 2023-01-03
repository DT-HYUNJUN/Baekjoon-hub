H, M = map(int, input().split())
res_H, res_M = 0, 0
alarm = 45
if M<45:
    res_M = M+60-alarm
    if H-1<0:
        res_H = 24+H-1
    else:
        res_H = H-1
else:
    res_H = H
    res_M = M-alarm
print(res_H, res_M)   