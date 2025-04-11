import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer, cur_idx, max_idx;
        Deque<Integer> queue = new ArrayDeque<>();
        List<Integer> pos = new ArrayList<>();
        
        for (int i=0; i<priorities.length; i++) queue.add(i);
        
        while(!queue.isEmpty()) {
            cur_idx = queue.pop();
            max_idx = Arrays.stream(priorities).max().getAsInt();
            
            if (priorities[cur_idx] < max_idx) queue.add(cur_idx);
            else {
                priorities[cur_idx] = -1;
                pos.add(cur_idx);
            }
        }
        answer = pos.indexOf(location) + 1;
        return answer;
    }
}