from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0, 1))

    while queue:
        x, y, dist = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny, dist + 1))
    
    return -1 
