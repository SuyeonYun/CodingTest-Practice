function solution(lottos, win_nums) {
    var answer = [];
    var rank = [6,6,5,4,3,2,1]
    let cnt_w = 0;
    let cnt_z = 0;
    for (let i = 0; i<lottos.length; i++) {
        if (win_nums.includes(lottos[i])) {
            cnt_w += 1;
        }
        if (lottos[i] == 0) cnt_z += 1;
    }
    answer.push(rank[cnt_w+cnt_z]);
    answer.push(rank[cnt_w]);
    
    return answer;
}