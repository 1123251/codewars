def find_height(cubes):
    first_layer = 0
    between = 1
    second_layer = 1
    lays = 0
    res = second_layer
    while res <= cubes:
        between += 1
        first_layer = second_layer
        second_layer = first_layer + between
        res += second_layer
        lays += 1
    return lays


true_ans = 18
print(find_height(1140))
