def solution(sequence):
    max_sum = 0
    min_sum = 0
    min_temp = 0
    max_temp = 0
    
    for i in range(len(sequence)):
        if i % 2 == 0:
            sequence[i] *= -1
            
    for s in sequence:
        max_temp += s
        if max_temp < 0:
            max_sum = 0
            max_temp = 0
        elif max_sum < max_temp:
            max_sum = max_temp
        
        min_temp -= s
        if min_temp < 0:
            min_sum = 0
            min_temp = 0
        elif min_sum < min_temp:
            min_sum = min_temp
            
    answer = max(min_sum, max_sum)
    return answer