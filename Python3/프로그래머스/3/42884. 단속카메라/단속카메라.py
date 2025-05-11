def solution(routes):
    routes.sort(key = lambda route: route[0])
    
    answer = 1
    prev_s = routes[0][0]
    prev_e = routes[0][1]
    routes.pop(0)
    
    for s, e in routes:
        if s > prev_e:
            answer += 1
            prev_e = e
        elif e < prev_e:
            prev_e = e
        prev_s = s
            
    return answer