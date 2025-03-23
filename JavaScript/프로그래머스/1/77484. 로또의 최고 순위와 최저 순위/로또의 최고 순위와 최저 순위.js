function solution(lottos, win_nums) {
    var answer = [];
    const rank = new Map();
    rank.set(6, 1);
    rank.set(5, 2);
    rank.set(4, 3);
    rank.set(3, 4);
    rank.set(2, 5);
    rank.set(1, 6);
    rank.set(0, 6);
    let cnt_w = 0;
    let cnt_z = 0;
    for (let i = 0; i<lottos.length; i++) {
        if (win_nums.includes(lottos[i])) {
            cnt_w += 1;
        }
        if (lottos[i] == 0) cnt_z += 1;
    }
    answer.push(rank.get(cnt_w + cnt_z));
    answer.push(rank.get(cnt_w));
    
    return answer;
}