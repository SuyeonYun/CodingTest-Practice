import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while(len(scoville) > 1):
        
        if scoville[0] >= K:
            return answer
        
        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)

    if scoville[0] >= K:
        return answer
    return -1