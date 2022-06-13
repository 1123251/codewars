def to_csv_text(row):
    str_row = ''
    for i in row:
        if row.index(i) != len(row)-1:
            str_row += str(i).strip('[] ').replace(' ', '')
            str_row += '\n'
    else:
        str_row += str(i).strip('][').replace(' ', '')
    return str_row


srow = [[0, 1, 2, 3, 45],
        [10, 11, 12, 13, 14],
        [20, 21, 22, 23, 24],
        [30, 31, 32, 33, 34]]
print(to_csv_text(srow))