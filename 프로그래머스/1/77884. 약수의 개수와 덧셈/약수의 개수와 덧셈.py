def solution(left, right):
    answer = 0
    sub_count = 0
    for i in range(left, right + 1):
        for j in range(1, i+1):
            if i % j == 0:
                sub_count += 1
        if sub_count & 1:
            answer -= i
        else:
            answer += i
        sub_count = 0
    return answer