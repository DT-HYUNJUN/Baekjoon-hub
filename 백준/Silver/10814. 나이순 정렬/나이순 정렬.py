import sys
N = int(input())
crew = []
for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    crew.append([age, name, i])
crew.sort(key=lambda x:(x[0], x[2]))
for i in crew:
    print(i[0], i[1])