import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int[] rank = {6,6,5,4,3,2,1};
        Map<Integer, Boolean> map = new HashMap<>();
        int cnt_z = 0;
        int cnt_w = 0;
        
        for (int lotto : lottos) {
            if (lotto == 0) {
                cnt_z += 1;
            }
            else map.put(lotto, true);
        }
        
        for (int num : win_nums) {
            if (map.containsKey(num)) cnt_w += 1;
        }
        
        answer[0] = rank[cnt_w + cnt_z];
        answer[1] = rank[cnt_w];
        return answer;
    }
}