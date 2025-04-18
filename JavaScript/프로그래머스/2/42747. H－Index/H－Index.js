function solution(citations) {
    var answer = 0;
    var cnt = citations.length;
    citations.sort((a, b) => b - a);

    for (let i=0; i <= citations[0]; i++) {
        if (i <= cnt) answer = i;
        let temp = 0;
        if (citations.includes(i)) {
            citations.forEach((c) => c == i ? temp++ : temp);
            cnt -= temp;
        }
    }
    return answer;
}