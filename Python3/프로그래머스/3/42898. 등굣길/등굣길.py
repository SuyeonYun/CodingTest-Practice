def solution(m, n, puddles):
    ways = [[0 for _ in range(m)] for _ in range(n)]
    ways[0][0] = 1
        
    for h in range(n):
        for w in range(m):
            if [w + 1, h + 1] in puddles:
                ways[h][w] = -1
                continue
            if 0 <= h - 1 and ways[h - 1][w] >= 0:
                ways[h][w] += ways[h - 1][w]
            if 0 <= w - 1 and ways[h][w - 1] >= 0:
                ways[h][w] += ways[h][w - 1]
    
    result = (ways[n - 1][m - 1]) % 1_000_000_007
    return result