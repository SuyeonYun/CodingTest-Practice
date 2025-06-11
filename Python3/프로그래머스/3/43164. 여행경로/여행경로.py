import copy

def isAllZero(double_list, n):
    for i in range(n):
        for j in range(n):
            if double_list[i][j] != 0:
                return False
    return True

def solution(tickets):
    idx = 0
    a_dict = {}
    r_dict = {}
    answer = []
    temp = set()
    
    for a, b in tickets:
        temp.add(a)
        temp.add(b)
    temp = list(temp)
    temp.sort()
    
    for t in temp:
        a_dict[t] = idx
        r_dict[idx] = t
        idx += 1
    
    l = len(a_dict)
    start = a_dict['ICN']
    
    info = [[0 for _ in range(l)] for _ in range(l)]
    for a, b in tickets:
        info[a_dict[a]][a_dict[b]] += 1
    
    def dfs(cur_idx, result):
        nonlocal info
        nonlocal answer
        
        if isAllZero(info, l):
            if len(answer) == 0:
                answer = result
            return
        
        cnt = 0
        for i in range(l):
            if info[cur_idx][i] > 0:
                cnt += 1
                info[cur_idx][i] -= 1
                temp = copy.deepcopy(result)
                temp.append(i)
                dfs(i, temp)
                info[cur_idx][i] += 1
        if cnt == 0:
            return
    
    dfs(start, [start])
    
    for i in range(len(answer)):
        answer[i] = r_dict[answer[i]]

    return answer
        