import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        int first, second;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i=0; i<scoville.length; i++) {
            pq.add(scoville[i]);
        }
        
        while (pq.size() > 1) {
            if (pq.peek() >= K) return answer;
            
            answer++;
            first = pq.poll();
            second = pq.poll();
            pq.add(first + second * 2);
        }
        
        if (pq.peek() >= K) return answer;
        return -1;
    }
}