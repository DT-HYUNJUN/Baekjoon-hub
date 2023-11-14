def solution(seoul):
    for idx, name in enumerate(seoul):
        if name == 'Kim':
            return f'김서방은 {idx}에 있다'