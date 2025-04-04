import java.util.*;

public class Solution {
    public static int solution(int n, int w, int num) {
        int min_h = n / w;
        int max_h = min_h + 1;
        int count_min = max_h * w - n;

        int cur_h = (num - 1) / w;
        int cur_w;

        if (cur_h % 2 == 0) {
            cur_w = (num - 1) % w;
        } else {
            cur_w = w * (cur_h + 1) - num;
        }

        List<Integer> min_idx = new ArrayList<>();
        for (int i = 0; i < count_min; i++) {
            if (max_h % 2 == 0) {
                min_idx.add(i);
            } else {
                min_idx.add(w - i - 1);
            }
        }

        if (min_idx.contains(cur_w)) {
            return min_h - cur_h;
        }
        return max_h - cur_h;
    }
}
