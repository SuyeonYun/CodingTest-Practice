import java.util.*;
import java.util.regex.*;

class Solution {
    public int[] solution(String s) {
        Map<String, Integer> map = new HashMap<>();
        Pattern p = Pattern.compile("\\d+");
        Matcher m = p.matcher(s);
        
        while (m.find()) {
            map.put(m.group(), map.getOrDefault(m.group(), 0) + 1);
        }
        int len = map.size();
        int[] answer = new int[len];
        for (String key : map.keySet()) {
            answer[len - map.get(key)] = Integer.parseInt(key);
        }
        
        return answer;
    }
}