function solution(s) {
    const allVal = [...s.match(/(\d+)/g)];
    const map = new Map();
    
    for (let i of allVal) {
        map.set(i, (map.get(i) || 0) + 1);
    };
    
    const sorted = [...map.entries()].sort((a, b) => b[1] - a[1]);    
    var answer = sorted.map(([key, value]) => Number(key));
    return answer;
}