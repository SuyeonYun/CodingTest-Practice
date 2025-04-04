function solution(n, w, num) {
    const min_h = Math.floor(n/w)
    const max_h = min_h + 1;
    const count_min = max_h * w - n;
    var cur_h = Math.floor((num - 1) / w);
    var cur_w;
    var min_idx = [];
    
    if (cur_h % 2 == 0) cur_w = (num - 1) % w;
    else cur_w = w*(cur_h + 1) - num;
    
    for (let i=0; i<count_min; i++) {
        if (max_h % 2 == 0) min_idx.push(i);
        else min_idx.push(w-i-1);
    }
    
    if (min_idx.includes(cur_w)) return min_h - cur_h;
    return max_h - cur_h;
}