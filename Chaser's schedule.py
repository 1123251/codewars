def solution(s, t):
    def get_slow_running(s, t):
        result = ((t - 1) * s) + s * 2
        return result

    def get_sprint_slise(s, t):
        sprint_slise = []
        i = s
        while (i * 2)+(i-1) >= s*2:
            if len(sprint_slise) >= t:
                break
            else:
                sprint_slise.append(i * 2)
                sprint_slise.append(i - 1)
                i -= 1
        while sprint_slise[-1] < s:
            sprint_slise.pop(-1)
        return sprint_slise

    def get_distance(sprint_slise, s, t):
        if len(sprint_slise) == t:
            result = sum(sprint_slise)
        else:
            result = (t - len(sprint_slise)) * s
            result += sum(sprint_slise)
        return result

    if s == 1 or s == 2:
        return get_slow_running(s, t)
    else:
        return get_distance(get_sprint_slise(s, t), s, t)


s = 19  # 728: 16660, 559: 10017, 19:1001
t = 49   # 15 : 16660, 12 : 10017, 49:1001
print(solution(s, t))
