A, B = map(int, input().split())
div, dn = 1, 2
while dn <= max(A, B):
    if A % dn == 0 and B % dn == 0:
        div *= dn
        A //= dn
        B //= dn        
    else:
        dn += 1
print(div)
print(div * A * B)