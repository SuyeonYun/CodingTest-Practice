function solution(s) {
    var answer = [];
    const pmap = new Map();
    for (let i = 0; i < s.length; i++) {
        if (pmap.has(s[i])) {
            answer.push(i - pmap.get(s[i]))
        }
        else {
            answer.push(-1)
        }
        pmap.set(s[i],i)
    }
    return answer;
}