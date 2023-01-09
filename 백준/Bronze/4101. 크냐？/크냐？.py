while True:    
    A, B = map(int, input().split())
    if A+B == 0:
        break
    else:        
        if A > B:
            print('Yes')
        else:
            print('No')