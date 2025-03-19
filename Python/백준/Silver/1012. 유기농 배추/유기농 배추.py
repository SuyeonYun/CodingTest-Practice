import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 4방향 (상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if field[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    # 배추 위치 기록 (입력: x, y -> field[y][x])
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    print(count)
