function solution(progresses, speeds) {
    var answer = [];
    var days = [];
    for (let i=0; i<speeds.length; i++) {
        let day = Math.ceil((100 - progresses[i]) / speeds[i]);
        days.push(day);
    }
    
    while (days.length != 0) {
        let temp = days.splice(0,1);
        let count = 1;
        for (let day of days) {
            if (day > temp) break;
            count += 1;
        }
        answer.push(count);
        days.splice(0, count-1);
    }
    return answer;
}