import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = list(x * (-1) for x in works)
    heapq.heapify(works)
    
    while n > 0:
        first = heapq.heappop(works)
        second = works[0]
        cnt = second - first + 1
        if cnt >= n:
            cnt = n
            
        heapq.heappush(works, first + cnt)
        n -= cnt
            
    return sum(x**2 for x in works)
                        