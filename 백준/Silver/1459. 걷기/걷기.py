X, Y, W, S = map(int, input().split())
parallel = (X + Y) * W
if (X + Y) & 1:
    if X > Y:
        diagnol = (X - 1) * S + W
    else:        
        diagnol = (Y - 1) * S + W
else:
    diagnol = max(X, Y) * S
if X > Y:
    mix = (Y * S) + (X - Y) * W
else:
    mix = (X * S) + (Y - X) * W
res = min(min(parallel, diagnol), mix)
print(res)
