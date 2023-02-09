def sudoku_check():
    # case row
    for row in sudoku:
        if set(row) != number:
            return 0
            
    # case col
    for i in range(9):
        temp = []
        for j in range(9):            
            temp.append(sudoku[j][i])
        if set(temp) != number:
            return 0
            
    # case pack
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            # pack start
            for a in range(3):
                for b in range(3):
                    temp.append(sudoku[i+a][j+b])
            if set(temp) != number:
                return 0            
    return 1

T = int(input())
for test_case in range(1, T+1):
    sudoku = [[int(x) for x in input().split()] for _ in range(9)]
    number = set([x for x in range(1, 10)])
    print(f'#{test_case} {sudoku_check()}')