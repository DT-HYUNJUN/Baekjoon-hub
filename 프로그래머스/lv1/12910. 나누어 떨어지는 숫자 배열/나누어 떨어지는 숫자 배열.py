def solution(arr, divisor):
    answer = []
    arr = sorted(arr)
    for i in arr:
        if not (i % divisor):
            answer.append(i)
    if answer:
        return answer
    else:
        return [-1]
    return answer