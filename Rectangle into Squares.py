def sqInRect(lng, wdth):
    rlist = []
    if lng == wdth:
        return None
    else:
        while lng != wdth:
            if lng > wdth:
                rlist.append(wdth)
                lng = lng - wdth
            else:
                rlist.append(lng)
                wdth = wdth - lng
        rlist.append(wdth)
        return rlist


print(sqInRect(20, 14))