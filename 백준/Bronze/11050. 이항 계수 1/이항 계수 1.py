def bino_coef(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return bino_coef(n-1, k-1) + bino_coef(n-1, k)
n, k = map(int, input().split())
print(bino_coef(n, k))