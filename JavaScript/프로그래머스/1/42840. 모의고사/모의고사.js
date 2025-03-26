function solution(answers) {
    var answer = [];
    var count = [-1,0,0,0];
    const ans_1 = [1, 2, 3, 4, 5];
    const ans_2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    for (let i=0; i<answers.length; i++){
        if (answers[i] == ans_1[i % ans_1.length]) count[1] += 1;
        if (answers[i] == ans_2[i % ans_2.length]) count[2] += 1;
        if (answers[i] == ans_3[i % ans_3.length]) count[3] += 1;   
    }
    
    var max = Math.max(...count);
    for (let j=1; j<count.length + 1; j++) {
        if (count[j] == max) answer.push(j);
    }
    return answer;
}