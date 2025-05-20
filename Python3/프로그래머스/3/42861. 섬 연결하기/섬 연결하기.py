import heapq

def solution(n, costs):
    info = []
    
    for i in range(n):
        info.append([])
        for j in range(n):
            if i == j:
                info[i].append(0)
            else:
                info[i].append(-1)
    
    for i, j, k in costs:
        info[i][j] = k
        info[j][i] = k
    
    result = []
    heap = [(0, 0, 0)]
    visited = [False] * n

    while len(result) < n:
        cur, s, e = heapq.heappop(heap)
        if visited[e]:
            continue
        result.append(cur)
        visited[e] = True

        for i in range(n):
            if not visited[i] and 0 < info[e][i]:
                heapq.heappush(heap, (info[e][i], e, i))

    return sum(result)
