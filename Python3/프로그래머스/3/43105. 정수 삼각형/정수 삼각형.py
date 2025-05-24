def solution(triangle):
    n = len(triangle)
    df = [[] for _ in range(n)]
    df[0].append(triangle[0][0])
    
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                df[i].append(df[i - 1][j] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                df[i].append(df[i - 1][j - 1] + triangle[i][j])
            else:
                df[i].append(max(df[i - 1][j - 1], df[i - 1][j]) + triangle[i][j])
    return max(df[n - 1])