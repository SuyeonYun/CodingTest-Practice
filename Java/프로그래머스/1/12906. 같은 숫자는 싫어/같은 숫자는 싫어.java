import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> a = new ArrayList<>();
        
        for (int i=0; i < arr.length; i++) {
            if (!a.isEmpty() && a.get(a.size() - 1) == arr[i]) continue;
            a.add(arr[i]);
        }
        
        int[] answer = new int[a.size()];
        for (int i = 0; i < a.size(); i ++) {
            answer[i] = a.get(i);
            }

        return answer;
    }
}