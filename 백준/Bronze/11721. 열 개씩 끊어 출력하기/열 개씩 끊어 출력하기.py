import math
string = input()
start, end = 0, 10
for i in range(math.ceil(len(string)/10)):
    print(string[start:end])
    start = end
    end += 10