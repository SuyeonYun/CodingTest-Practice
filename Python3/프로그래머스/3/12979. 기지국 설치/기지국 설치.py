import math

def solution(n, stations, w):
    answer = 0
    start = 0 - w
    if stations[-1] != n:
        stations.append(n + w + 1)
        
    for end in stations:
        cnt = end - start - 1 - 2 * w
        if cnt > 0:
            answer += math.ceil((cnt) / (2 * w + 1))
        start = end

    return answer