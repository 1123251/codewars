pyramid = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
for i in range(len(pyramid)-2, -1, -1):
    for j in range(i+1):
        pyramid[i][j] += max(pyramid[i+1][j], pyramid[i+1][j+1])
print(pyramid[0][0])
