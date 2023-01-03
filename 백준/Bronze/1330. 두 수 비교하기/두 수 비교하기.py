A, B = map(int, input().split())
if A > B:
    res = '>'
elif A < B:
    res = '<'
else:
    res='=='

print(res)