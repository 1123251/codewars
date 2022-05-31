def same_factRev(nMax):
    while nMax != 1088:
        if str(nMax) != str(nMax)[::-1]:
            rang = 19
            for i in range(2, rang+1):
                if nMax % i == 0:
                    print(i)
                if int(str(nMax)[::-1]) % i == 0:
                    print(i)
        nMax -= 1
    return nMax


exclusion = ['palindrom', len('1'), 0 < 1000]
print(same_factRev(1089))
