import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        int count = 0;
        Stack<Integer> stack = new Stack<>();
        
        for (int ing : ingredient) {
            stack.push(ing);
            int j = stack.size();
            if (j >= 4) {
                if (stack.get(j - 4) == 1 &&
                   stack.get(j - 3) == 2 &&
                   stack.get(j - 2) == 3 &&
                   stack.get(j - 1) == 1) {
                    count ++;
                    
                    for (int i = 0; i < 4; i++) stack.pop();
                }
            }
        }
        return count;
    }
}