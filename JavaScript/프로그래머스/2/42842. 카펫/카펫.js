function solution(brown, yellow) {
    const plus = (brown + 4) / 2;
    const mul = brown + yellow;
    
    for (let x=1; x<plus; x++) {
        let y = plus - x;
        if (x * y == mul) return [y, x];
    }
}