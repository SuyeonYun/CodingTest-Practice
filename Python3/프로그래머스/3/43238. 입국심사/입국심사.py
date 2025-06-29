def solution(n, times):
    answer = -1
    times.sort()
    
    def binary_search(min_n, max_n):
        nonlocal answer
        if min_n >= max_n :
            return
        
        mid = (min_n + max_n) // 2
        sum_n = 0
        for t in times:
            sum_n += mid // t
            
        if sum_n >= n:
            answer = mid
            binary_search(min_n, mid)
        else:
            binary_search(mid + 1, max_n)          
    
    binary_search(0, max(times) * n)
    return answer
