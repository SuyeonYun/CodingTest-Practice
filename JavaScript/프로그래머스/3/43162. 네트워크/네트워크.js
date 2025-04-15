function solution(n, computers) {
    var cur, idx;
    var answer = 0;
    var total = [];
    var queue = [];
    for (let i=0; i<n; i++) total.push(1);
    
    while (total.includes(1)) {
        answer++;
        idx = total.findIndex((e) => e == 1);
        total[idx] = -1
        queue.push(idx);
        while (queue.length > 0) {
            cur = queue.shift();
            for (let i=0; i<n; i++) {
                if (computers[cur][i] == 1 && total[i] == 1) {
                    queue.push(i);
                    total[cur] = -1;
                    computers[cur][i] = 0;
                    computers[i][cur] = 0;
                }
            }
        }
    }
    
    return answer;
}