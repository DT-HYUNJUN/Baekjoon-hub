total = 0
mxm = 0
for _ in range(4):
    get_off, get_on = map(int, input().split())
    total = total - get_off + get_on
    if mxm < total:
        mxm = total
print(mxm)