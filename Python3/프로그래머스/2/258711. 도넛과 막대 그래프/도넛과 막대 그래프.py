def solution(edges):
    donut = 0
    stick = 0
    eight = 0
    n = max(max(row) for row in edges)
    
    result = []
    inbound = [[] for _ in range(n+1)]
    outbound = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    
    for a, b in edges:
        outbound[a].append(b)
        inbound[b].append(a)
        
    for i in range(1, n):
        if len(inbound[i]) == 0 and len(outbound[i]) >= 2:
            stranger = i
            break
            
    for cur in outbound[stranger]:
        while(True):
            if len(outbound[cur]) == 0:
                stick +=1
                break
                
            if len(outbound[cur]) > 1:
                eight += 1
                break
                
            if visited[cur]:
                donut += 1
                break
                
            visited[cur] = True
            cur = outbound[cur][0]

    result.append(stranger)
    result.append(donut)
    result.append(stick)
    result.append(eight)
        
    return result
    