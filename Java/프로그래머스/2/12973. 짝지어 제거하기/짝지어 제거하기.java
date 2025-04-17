import java.util.*;

class Solution
{
    public int solution(String s)
    {
        List<Character> stack = new ArrayList<>();
        int idx = 0;
        int l;
        
        while (idx < s.length()) {
            stack.add(s.charAt(idx++));
            l = stack.size();
            
            if (l >= 2 && stack.get(l - 1) == stack.get(l - 2)) {
                stack.remove(l - 1);
                stack.remove(stack.size() - 1);
            }
        }
        
        if (stack.isEmpty()) return 1;
        return 0;
    }
}