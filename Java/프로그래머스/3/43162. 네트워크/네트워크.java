import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int cur, idx;
        List<Integer> total = new ArrayList<>();
        Deque<Integer> queue = new ArrayDeque<>();
        
        for (int i=0; i<n; i++) total.add(i);
        
        while (!total.isEmpty()) {
            answer++;
            queue.add(total.remove(0));
            while (!queue.isEmpty()) {
                cur = queue.pop();
                for (int i=0; i<n; i++) {
                    if (computers[cur][i] == 1 && total.contains(i)) {
                     queue.add(i);
                     total.remove((Object) i);
                     computers[cur][i] = 0;
                     computers[i][cur] = 0;
                    }
                }
            }
        }
        return answer;
    }
}