H, M = map(int, input().split())
C = int(input())
res_H = H
res_M = M+C

if M+C<60:
    print(H, M+C)
else:    
    while res_M>=60:
        res_M = res_M-60
        res_H = res_H+1
        if res_H>=24:
            res_H = res_H-24
    print(res_H, res_M)