from collections import deque
def solution(n, computers):
    answer = 0
    q = deque()
    visited = [False for _ in range(n)]
    for i in range(n):
        computers[i][i] = 0
    
    while False in visited:
        answer += 1
        q.append(visited.index(False))
        
        while q:
            cur = q.popleft()
            if visited[cur]:
                continue
            visited[cur] = True
            
            for i in range(n):
                if not visited[i] and computers[cur][i]:
                    q.append(i)
                      
    return answer
                    
            
            