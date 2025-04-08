import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> a = new ArrayList<>();
        List<Integer> days = new ArrayList<>();
        
        for (int i=0; i<speeds.length; i++) {
            Double d = Math.ceil((100.0 - progresses[i]) / speeds[i]);
            int div = d.intValue();
            days.add(div);
        }
        
        while (!days.isEmpty()) {
            int temp = days.remove(0);
            int count = 1;
            for (int day : days) {
                if (day > temp) break;
                count += 1;
            }
            a.add(count);
            for (int i=1; i<count; i++) days.remove(0);
        }
        
        int[] answer = new int[a.size()];
        for (int i=0; i<answer.length; i++) {
            answer[i] = a.get(i);
        }
        return answer;
    }
}