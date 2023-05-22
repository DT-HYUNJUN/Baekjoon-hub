S = sorted(input())
count = S.count('0')
S_zero = S[:count]
S_one = S[count:]
S_zero_half = int(len(S_zero) / 2)
S_one_half = int(len(S_one) / 2)
new_S = S_zero[:S_zero_half] + S_one[:S_one_half]
print(''.join(new_S))