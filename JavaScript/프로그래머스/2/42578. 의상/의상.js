function solution(clothes) {
    var answer = 1;
    const index = [];
    const result = [];
    
    for (let cloth of clothes) {
        const category = cloth[1];
        if (index.includes(category)) result[index.indexOf(category)] += 1;
        else {
            index.push(category);
            result.push(1);
        }
    }
    
    for (let value of result) answer *= (value + 1);
    
    return answer - 1;
}