from collections import deque

def solution(board):
    n = len(board)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((0, 0, 0, -1))
    total_cost = [[[float('inf'), float('inf')] for _ in range(n)] for _ in range(n)]
    
    while queue:
        x, y, cost, prev_direction = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if i <= 1:
                diff = 1
                nd = 0
            else:
                diff = 0
                nd = 1
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if prev_direction == diff:
                    nc = cost + 600
                else:
                    nc = cost + 100
                    
                if total_cost[nx][ny][nd] > nc:
                    total_cost[nx][ny][nd] = nc
                    queue.append((nx, ny, nc, nd))

    return min(total_cost[-1][-1])
