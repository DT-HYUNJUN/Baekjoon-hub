def solution(num):
    answer = 0
    count = 0
    if num == 1:
        return 0
    while True:
        if num == 1:
            break
        if count == 500:
            return -1
        if num & 1:
            num = (num * 3) + 1
        else:
            num = num // 2
        count = count + 1
    answer = count
    return answer