import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Map<Character, Integer> pmap = new HashMap<>();
        for (int i=0; i < s.length(); i++) {
            if (pmap.containsKey(s.charAt(i))) {
                answer[i] = i - pmap.get(s.charAt(i));
            }
            else {
                answer[i] = -1;
            }
            pmap.put(s.charAt(i), i);
        }
        return answer;
    }
}