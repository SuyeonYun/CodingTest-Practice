import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> match = new HashMap<>();
        for (int i=0; i<participant.length; i++) {
            match.put(participant[i], match.getOrDefault(participant[i], 0) + 1);
            if (i < completion.length) {
                match.put(completion[i], match.getOrDefault(completion[i], 0) - 1);
            }
        }
        
        for (Map.Entry<String, Integer> entry: match.entrySet()) {
            if (entry.getValue() > 0) {
                return entry.getKey();
            }
        }
        return answer;
    }
}