import heapq

def solution(n, costs):
    queue = []
    start = 0
    answer = 0
    visited = [False for _ in range(n)]
    
    info = [[float('inf') for _ in range(n)] for _ in range(n)]
    for x, y, cost in costs:
        info[x][y] = cost
        info[y][x] = cost
    
    for i in range(n):
        info[i][i] = 0
    
    heapq.heappush(queue, (info[start][start], start, start))
    
    while queue:
        cur_dist, start, end = heapq.heappop(queue)
        if visited[end]:
            continue
        answer += info[start][end]
        visited[end] = True
        for i in range(n):
            if not visited[i] and info[end][i] != float('inf'):
                heapq.heappush(queue, (info[end][i], end, i))

    return answer
    