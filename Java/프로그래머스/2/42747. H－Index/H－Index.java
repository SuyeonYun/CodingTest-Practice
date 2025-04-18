import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int temp;
        int answer = 0;
        int cnt = citations.length;
        
        List<Integer> c = new ArrayList<>();
        for (int i=0; i<citations.length; i++) {
            c.add(citations[i]);
        }        
        c.sort((a, b) -> b - a);

        for (int i=0; i <= c.get(0); i++) {
            temp = 0;
            if (i <= cnt) answer = i;
            if (c.contains(i)) {
                final int target = i;
                long count = c.stream().filter(e -> e == target).count();
                cnt -= count;
            }
        }
        return answer;
    }
}