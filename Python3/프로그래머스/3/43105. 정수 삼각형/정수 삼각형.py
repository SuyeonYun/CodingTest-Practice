def solution(triangle):
    
    for depth in range(1, len(triangle)):
        length = len(triangle[depth])
        before = triangle[depth - 1]
        for idx in range(length):
            if idx == 0:
                triangle[depth][idx] += before[idx]
            elif idx == length - 1:
                triangle[depth][idx] += before[idx - 1]
            else:
                triangle[depth][idx] += max(before[idx], before[idx - 1])
    
    return max(triangle[-1])
        