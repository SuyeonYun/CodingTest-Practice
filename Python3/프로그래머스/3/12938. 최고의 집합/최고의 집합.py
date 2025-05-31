def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    while n > 0:
        temp = int(s / n)
        answer.append(temp)
        s -= temp
        n -= 1
    
    return answer