pyramid = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
reversed_pyramid = pyramid[::-1]

for current_level, next_level in zip(reversed_pyramid[:-1], reversed_pyramid[1:]):
    for i in range(len(current_level) - 1):
        left, right = current_level[i], current_level[i+1]
        next_level[i] += max(left, right)

print(pyramid[0][0])



