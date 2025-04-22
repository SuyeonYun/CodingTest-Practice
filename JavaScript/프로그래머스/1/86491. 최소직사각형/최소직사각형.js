function solution(sizes) {
    for (let size of sizes) {
        size.sort((a, b) => a - b);
    }
    
    let max_w = 0;
    let max_h = 0;
    for (let i=0; i<sizes.length; i++) {
        if (sizes[i][0] > max_w) max_w = sizes[i][0];
        if (sizes[i][1] > max_h) max_h = sizes[i][1];
    }
    
    return max_w * max_h;
}