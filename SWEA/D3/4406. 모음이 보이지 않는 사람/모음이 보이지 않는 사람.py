T = int(input())
for test_case in range(1, T+1):
    word = input()
    for char in word:
        if char in "aeiou":
            word = word.replace(char, '')
    print(f'#{test_case} {word}')