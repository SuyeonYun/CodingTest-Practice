def solution(n, edge):
    q = []
    edges = [[] * x for x in range(n)]
    visited = [False * x for x in range(n)]
    dist = [float('inf') * x for x in range(n)]
    
    q.append(0)
    dist[0] = 0
    
    for s, e in edge: 
        edges[s - 1].append(e - 1)
        edges[e - 1].append(s - 1)
    
    for arr in edges:
        arr.sort()

    while len(q) > 0:
        cur = q.pop(0)
        if not visited[cur]:
            visited[cur] = True
            for i in edges[cur]:
                dist[i] = min(dist[i], dist[cur] + 1)
                q.append(i)
    
    max_d = max(dist)
    return dist.count(max_d)