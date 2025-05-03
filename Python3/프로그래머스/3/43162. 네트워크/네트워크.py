def solution(n, computers):
    visited = [False] * n
    root_arr = []
    result = 0

    def dfs(idx, root):
        nonlocal result
        visited[idx] = True
        count = 0
        for i in range(n):
            if computers[idx][i] == 1 and not visited[i]:
                count += 1
                dfs(i, root)
        if count == 0 and root not in root_arr:
            result += 1
            root_arr.append(root)
        return
    
    for i in range(n):
        if not visited[i]:
            dfs(i, i)  
    return result
    
        