def valid_solution(sudoku):
    def get_square(sudoku, i, j):
        res_list = []
        x = i // 3
        y = j // 3
        for a in sudoku[x * 3:(x + 1) * 3]:
            res_list.extend(a[y * 3:(y + 1) * 3])
        return res_list

    def get_column(sudoku, i):
        res_list = []
        for a in sudoku:
            res_list.append(a[i])
        return res_list

    def get_row(sudoku, i):
        return sudoku[i]

    for i in range(0, 9):
        if 0 in get_row(sudoku, i):
            return False
    for i in range(0, 9):
        if len(get_row(sudoku, i)) != len(set(get_row(sudoku, i))):
            return False
        elif len(get_column(sudoku, i)) != len(set(get_column(sudoku, i))):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if len(get_square(sudoku, i, j)) != len(set(get_square(sudoku, i, j))):
                return False
            else:
                return True


sudoku = (([[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution(sudoku))



