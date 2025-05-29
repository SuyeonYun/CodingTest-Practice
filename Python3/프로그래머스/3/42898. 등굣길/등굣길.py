def solution(m, n, puddles):
    info = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    info[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [i , j] == [1, 1]:
                continue
            info[i][j] = info[i - 1][j] + info[i][j - 1]
            if [j, i] in puddles:
                info[i][j] = 0
                
    return info[n][m] % 1_000_000_007