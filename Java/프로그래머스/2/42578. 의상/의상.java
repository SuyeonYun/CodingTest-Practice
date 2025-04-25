import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> dict = new HashMap<>();
        
        for (String[] cloth : clothes) {
            dict.put(cloth[1], dict.getOrDefault(cloth[1], 0) + 1);
        }
        
        for (int value : dict.values()) {
            answer *= (value + 1);
        }
        
        return answer - 1;
    }
}