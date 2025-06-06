def solution(gems):
    answer = [1, len(gems)]
    g_dict = {}
    for gem in gems:
        g_dict[gem] = 0
    
    s = 0
    g_set = set()
    for e in range(len(gems)):
        g_dict[gems[e]] += 1
        g_set.add(gems[e])
        if len(g_set) == len(g_dict):
            for i in range(s, e + 1):
                if g_dict[gems[s]] == 1:
                    if answer[1] - answer[0] > e - s:
                        answer = [s + 1, e + 1]
                    break
                else:
                    g_dict[gems[s]] -= 1
                    s += 1
                
    return answer
