from collections import deque

def solution(board):
    n = len(board)
    queue = deque()
    queue.append((0, 0, 0, ''))
    total_cost = [[[float('inf'), float('inf')] for _ in range(n)] for _ in range(n)]
    
    while queue:
        x, y, cost, prev_direction = queue.popleft()
        
        if 0 <= x - 1 < n and board[x - 1][y] == 0:
            if prev_direction == 'y':
                if total_cost[x - 1][y][0] > cost + 600:
                    total_cost[x - 1][y][0] = cost + 600
                    queue.append((x - 1, y, cost + 600, 'x'))
            else:
                if total_cost[x - 1][y][0] > cost + 100:
                    total_cost[x - 1][y][0] = cost + 100
                    queue.append((x - 1, y, cost + 100, 'x'))
        
        if 0 <= x + 1 < n and board[x + 1][y] == 0:
            if prev_direction == 'y':
                if total_cost[x + 1][y][0] > cost + 600:
                    total_cost[x + 1][y][0] = cost + 600
                    queue.append((x + 1, y, cost + 600, 'x'))
            else:
                if total_cost[x + 1][y][0] > cost + 100:
                    total_cost[x + 1][y][0] = cost + 100
                    queue.append((x + 1, y, cost + 100, 'x'))
                
        if 0 <= y - 1 < n and board[x][y - 1] == 0:
            if prev_direction == 'x':
                if total_cost[x][y - 1][1] > cost + 600:
                    total_cost[x][y - 1][1] = cost + 600
                    queue.append((x, y - 1, cost + 600, 'y'))
            else:
                if total_cost[x][y - 1][1] > cost + 100:
                    total_cost[x][y - 1][1] = cost + 100
                    queue.append((x, y - 1, cost + 100, 'y'))
                
        if 0 <= y + 1 < n and board[x][y + 1] == 0:
            if prev_direction == 'x':
                if total_cost[x][y + 1][1] > cost + 600:
                    total_cost[x][y + 1][1] = cost + 600
                    queue.append((x, y + 1, cost + 600, 'y'))
            else:
                if total_cost[x][y + 1][1] > cost + 100:
                    total_cost[x][y + 1][1] = cost + 100
                    queue.append((x, y + 1, cost + 100, 'y'))
                    
    return min(total_cost[-1][-1])
