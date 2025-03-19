import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y):
    visited[x][y] = 1
    h_num = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if field[nx][ny] == 1 and visited[nx][ny] == 0:
                h_num += dfs(nx, ny)
    return h_num

N = int(input().strip())
field = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    string = input().strip()
    for j in range(N):
        field[i][j] = int(string[j])
        
count = 0
num_arr = []
for i in range(N):
    for j in range(N):
        if field[i][j] == 1 and visited[i][j] == 0:
            num_arr.append(dfs(i, j))
            count += 1
print(count)
                
num_arr.sort()
for num in num_arr:
    print(num)
            
        