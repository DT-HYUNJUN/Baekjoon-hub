while 1:
    S = input()
    if S == '0':
        break
    else:
        for i in range(len(S)):
            if S[i] == S[-i-1]:
                continue
            else:
                print('no')
                break
        else:
            print('yes')            