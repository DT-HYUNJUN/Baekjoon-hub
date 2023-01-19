import sys
lst = [int(x) for x in sys.stdin.readlines() if int(x) & 1]
if lst:
    print(sum(lst), min(lst), sep='\n')
else:
    print(-1)