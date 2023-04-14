N = int(input())
answer = []
max_num = 0
for i in range(N, -1, -1):
    first = N
    second = i
    tmp = [first, second]
    index = 0
    while True:
        if tmp[index] - tmp[index + 1] < 0:
            break
        third = tmp[index] - tmp[index+1]
        tmp.append(third)
        index += 1
    length = len(tmp)
    if max_num <= length:
        max_num = length
        answer = [length] + tmp
print(answer[0])
print(' '.join(map(str, answer[1:])))