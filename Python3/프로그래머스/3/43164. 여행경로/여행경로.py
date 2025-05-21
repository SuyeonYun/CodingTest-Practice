import copy
def solution(tickets):
    answer = []
    temp = set()
    d_dict = {}
    r_dict = {}
    
    for s, e in tickets:
        temp.add(s)
        temp.add(e)
    temp = list(temp)
    temp.sort()

    for i in range(len(temp)):
        d_dict[temp[i]] = i
    
    for i in range(len(tickets)):
        tickets[i][0] = d_dict[tickets[i][0]]
        tickets[i][1] = d_dict[tickets[i][1]]
        
    for k, v in d_dict.items():
        r_dict[v] = k
    
    n = len(d_dict)
        
    INFO = [[0 for _ in range(n)] for _ in range(n)] 
    
    for s, e in tickets:
        INFO[s][e] += 1

    def dfs(start, info, result):
        nonlocal answer
        result.append(start)
        if not any(x > 0 for row in info for x in row):
            if not answer:
                #print(f'start: {start}, info: {info}, result: {result}')
                answer = result
        for end in range(n):
            if info[start][end] > 0:
                info[start][end] -= 1
                dfs(end, copy.deepcopy(info), copy.deepcopy(result))
                info[start][end] += 1
                
    dfs(d_dict['ICN'], INFO, [])
    
    for i in range(len(answer)):
        answer[i] = r_dict[answer[i]]

    return answer