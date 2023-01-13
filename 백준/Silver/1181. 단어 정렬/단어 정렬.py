import sys
n = int(sys.stdin.readline())
word = list(set(str(sys.stdin.readline().strip()) for _ in range(n)))
word.sort()
word.sort(key=lambda x: len(x))
for i in word:
    print(i)