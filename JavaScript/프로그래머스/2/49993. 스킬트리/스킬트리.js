function solution(skill, skill_trees) {
    var answer = 0;
    var temp, s_temp, idx, i;
    for (let ex of skill_trees) {
        temp = [];
        for (let str of skill) {
            i = ex.search(str);
            idx = (i == -1) ? Infinity : i;
            temp.push(idx);
        }
        s_temp = [...temp].sort((a,b) => a - b);
        if (JSON.stringify(temp) == JSON.stringify(s_temp)) answer++;
    }
    
    return answer;
}