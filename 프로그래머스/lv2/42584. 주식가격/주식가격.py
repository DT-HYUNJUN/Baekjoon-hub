from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        tmp = 0
        price = prices.popleft()
        
        for i in prices:
            tmp += 1
            if price > i:
                break
        answer.append(tmp)
    return answer
