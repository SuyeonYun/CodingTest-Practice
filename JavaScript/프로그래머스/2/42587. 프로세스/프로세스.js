function solution(priorities, location) {
    var queue = [];
    var pos = [];
    var cur_idx, max_idx, answer;
    
    for (let i=0; i<priorities.length; i++) queue.push(i);

    while(queue.length > 0) {
        cur_idx = queue.shift();
        max_idx = Math.max(...priorities);
        
        if (priorities[cur_idx] < max_idx) queue.push(cur_idx);
        else {
            pos.push(cur_idx);
            priorities[cur_idx] = -1;
        }
    }
    answer = pos.indexOf(location) + 1;
    return answer;
}