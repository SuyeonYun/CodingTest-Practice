from collections import deque

def solution(n, edge):
    start = 0
    dist = [-1 for _ in range(n)]
    info = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = deque()
    queue.append((start, start))
    
    for x, y in edge:
        info[x - 1].append(y - 1)
        info[y - 1].append(x - 1)
    
    while queue:
        prev, cur = queue.popleft()
        if visited[cur]:
            continue
        visited[cur] = True
        dist[cur] = dist[prev] + 1
        
        for i in info[cur]:
            if not visited[i]:
                queue.append((cur, i))
    
    max_dist = max(dist)
    answer = dist.count(max_dist)
    return answer
