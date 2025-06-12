from collections import deque

def solution(n, roads, sources, destination):
    start = destination - 1
    answer = []
    queue = deque()
    dist = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    
    info = [[] for _ in range(n)]
    for x, y in roads:
        info[x - 1].append(y - 1)
        info[y - 1].append(x - 1)
    
    queue.append((start, start))
    while queue:
        prev, cur = queue.popleft()
        if visited[cur]:
            continue
        visited[cur] = True
        dist[cur] = dist[prev] + 1
        
        for idx in info[cur]:
            if not visited[idx]:
                queue.append((cur, idx))
    
    for s in sources:
        answer.append(dist[s - 1])
        
    return answer
