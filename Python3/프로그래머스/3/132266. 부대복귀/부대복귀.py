from collections import deque

def solution(n, roads, sources, destination):
    q = deque()
    answer = []
    visited = [False for _ in range(n)]
    dist = [-1 for _ in range(n)]
    info = [[] for _ in range(n)]
    for x, y in roads:
        info[x - 1].append(y - 1)
        info[y - 1].append(x - 1)
    
    cur = destination - 1
    prev = destination - 1
    q.append((prev, cur))
    while len(q) > 0 :
        prev, cur = q.popleft()
        if visited[cur]:
            continue
        visited[cur] = True
        dist[cur] = dist[prev] + 1
        for i in info[cur]:
            if not visited[i]:
                q.append((cur, i))
                
    for s in sources:
        answer.append(dist[s - 1])

    return answer