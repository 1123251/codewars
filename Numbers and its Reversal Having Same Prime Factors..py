#time limit trouble

def same_factRev(nMax):
    list_max = []
    while nMax != 10898:
        if str(nMax) != str(nMax)[::-1]:
            a, b, i, j = nMax, int(str(nMax)[::-1]), 2, 2
            set_one = set()
            set_two = set()
            while a != 1:
                if a % i == 0:
                    a = a / i
                    set_one.add(i)
                    i = 2
                else:
                    i += 1
            while b != 1:
                if b % j == 0:
                    b = b / j
                    set_two.add(j)
                    j = 2
                else:
                    j += 1
            if set_one == set_two:
                list_max.append(nMax)
            set_two = set()
            set_one = set()
        nMax -= 1
    print(set_two, set_one)
    return sorted(list_max)


print(same_factRev(10989))
