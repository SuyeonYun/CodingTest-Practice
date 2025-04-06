import java.util.*;

class Solution {
    public boolean is_right(String str, Integer start_idx) {
        Deque<Character> stack = new ArrayDeque<Character>();
        Character cur, last;
        for (int i=start_idx; i<start_idx + str.length()/2; i++) {
            cur = str.charAt(i);
            last = stack.peek();
            if (stack.size() != 0) {
                if ((cur == ')' && last == '(')
                   || (cur == '}' && last == '{')
                   || (cur == ']' && last == '[')) {
                    stack.pop();
                    continue;
                }
            }
            stack.push(str.charAt(i));
        }
        if (stack.size() == 0) return true;
        return false;
    }
    
    public int solution(String s) {
        int answer = 0;
        s += s;
        for (int i=0; i<s.length()/2; i++) {
            if (is_right(s, i)) answer += 1;
        }
        return answer;
    }
}