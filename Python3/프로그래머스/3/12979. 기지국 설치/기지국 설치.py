import math

def solution(n, stations, w):
    answer = 0
    rest = []
    
    start = 0
    for s in stations:
        rest.append(s - w - 1 - start)
        start = s + w
    if start < n:
        rest.append(n - start)
        
    for r in rest:
        answer += math.ceil(r / (w * 2 + 1))

    return answer