function solution(s) {
    const allVal = [...s.match(/(\d+)/g)];
    const map = new Map();
    
    for (let i of allVal) {
        map.set(i, (map.get(i) || 0) + 1);
    };
    
    const len = map.size;
    var answer = new Array(len);
    
    map.forEach((value, key) => answer[len - value] = parseInt(key));
    return answer;
}