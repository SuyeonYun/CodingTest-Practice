import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        List<String> temp = new ArrayList();
        String[] answer = new String[strings.length];
        for (int i=0; i<strings.length; i++) {
            temp.add(strings[i]);
        }
        temp.sort((a,b) -> {
            if (a.charAt(n) == b.charAt(n)) return a.compareTo(b);
            return Character.compare(a.charAt(n), b.charAt(n));
        });
        for (int i=0; i<strings.length; i++) {
            answer[i] = temp.get(i);
        }
        
        return answer;
    }
}