import math

def solution(n, s):
    answer = []
    result = 0
    
    if n > s:
        return [-1]
    
    while n > 0:
        result = math.floor(s / n)
        answer.append(result)
        s -= result
        n -= 1
    
    answer.sort()
    return answer