def solution(sequence):
    sum_r = 0
    max_r = 0
    min_r = 1
    for i in range(len(sequence)):
        if i % 2 == 0:
            sequence[i] *= -1
            
    for s in sequence:
        sum_r += s
        if sum_r < 0:
            sum_r = 0
        if sum_r > max_r:
            max_r = sum_r
            
    sum_r = 0
    for s in sequence:
        sum_r += s
        if sum_r > 0:
            sum_r = 0
        if sum_r < min_r:
            min_r = sum_r  
            
    return max(-min_r, max_r)