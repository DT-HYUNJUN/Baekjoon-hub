import sys
print(*sorted([x for x in sys.stdin.readline()], reverse=True), sep='')