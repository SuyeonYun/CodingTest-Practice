function solution(numbers, target) {
    var answer = 0;
    
    function dfs(index, total) {
        if (index == numbers.length) {
            if (total == target) answer += 1;
            return;
        }
        
        dfs(index + 1, total + numbers[index]);
        dfs(index + 1, total - numbers[index]);
    }
    
    dfs(0, 0);
    return answer;
}