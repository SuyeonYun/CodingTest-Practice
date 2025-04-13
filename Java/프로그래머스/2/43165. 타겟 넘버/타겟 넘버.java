import java.util.*;

class Solution {
    int answer = 0;
    int[] numbers;
    int target;
    
    public void dfs(int index, int total) {
        if (index == numbers.length) {
            if (total == target) answer++;
            return;
        }

        dfs(index + 1, total + numbers[index]);
        dfs(index + 1, total - numbers[index]);
    }
    
    public int solution(int[] numbers, int target) {
        this.numbers = numbers;
        this.target = target;
        answer = 0;
        
        dfs(0, 0);
        return answer;
    }
}