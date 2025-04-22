import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        for (int[] size : sizes) {
            Arrays.sort(size);
        }
        
        int max_w = 0;
        int max_h = 0;
        for (int i=0; i<sizes.length; i++) {
            if (max_w < sizes[i][0]) max_w = sizes[i][0];
            if (max_h < sizes[i][1]) max_h = sizes[i][1];
        }
        
        return max_w * max_h;
    }
}