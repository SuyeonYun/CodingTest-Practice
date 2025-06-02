def solution(routes):
    routes.sort(key = lambda x: x[1])
    idx = 1
    answer = 1
    cur = routes[0][1]
    while idx < len(routes):
        start = routes[idx][0]
        end = routes[idx][1]
        if start > cur:
            cur = end
            answer += 1
        idx += 1
            
    return answer