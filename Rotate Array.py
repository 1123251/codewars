def rotate(data, n):
    if n < -len(data) and n < 0:
        n = - n
        while (n > len(data)) and (len(data) > 0):
            n = n // len(data)
        n = -n
    else:
        while (n > len(data)) and (len(data) > 0):
            n = n // len(data)
    result = []
    left_slise = data[-n:]
    right_slise = data[:-n]
    result.extend(left_slise)
    result.extend(right_slise)
    return result


data2 = [1, 2, 3, 4, 5, 6]
n = 0
print(data2[-n:])
print(data2[:-n])
print(rotate(data2, -1))

