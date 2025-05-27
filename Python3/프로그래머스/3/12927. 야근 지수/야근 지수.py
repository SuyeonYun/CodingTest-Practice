import heapq

def solution(n, works):
    works = [-i for i in works]
    heapq.heapify(works)
    for i in range(n):
        if len(works) == 0:
            return 0
        temp = heapq.heappop(works)
        temp += 1
        if temp != 0:
            heapq.heappush(works, temp)
    
    answer = sum([i**2 for i in works])
    return answer