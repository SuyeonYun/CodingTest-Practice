function dfs(dungeons, visited, k, cnt = 0) {
    let max_cnt = cnt;
    
    for (let i=0; i<dungeons.length; i++) {
        let st = dungeons[i][0];
        let need = dungeons[i][1];
        
        if (!visited[i] && k >= st) {
            visited[i] = true;
            const result = dfs(dungeons, visited, k - need, cnt + 1);
            visited[i] = false;
            
            max_cnt = Math.max(max_cnt, result);
        }
    }
    return max_cnt;
}

function solution(k, dungeons) {
    const visited = new Array(dungeons.length).fill(false);
    let answer = dfs(dungeons, visited, k);
    return answer;
}