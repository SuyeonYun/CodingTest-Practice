function solution(array, commands) {
    var answer = [];
    var temp = [];
    let i,j,k;
    for (com of commands) {
        i = com[0] - 1;
        j = com[1];
        k = com[2] - 1;
        
        temp = array.slice(i, j);
        temp.sort((a,b) => a - b);
        answer.push(temp[k])
    }
    return answer;
}