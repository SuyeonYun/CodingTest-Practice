import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        List<Integer> count = new ArrayList<>(Arrays.asList(-1,0,0,0));
        int[] ans_1 = {1, 2, 3, 4, 5};
        int[] ans_2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] ans_3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        for (int i=0; i<answers.length; i++) {
            if (answers[i] == ans_1[i % ans_1.length]) count.set(1, count.get(1) + 1);
            if (answers[i] == ans_2[i % ans_2.length]) count.set(2, count.get(2) + 1);
            if (answers[i] == ans_3[i % ans_3.length]) count.set(3, count.get(3) + 1);
        }
        
        int max_num = Collections.max(count);
        
        for (int j=1; j<count.size(); j++) {
            if (count.get(j) == max_num) {
                answer.add(j);
            }
        }
        
        int[] ret = new int[answer.size()];
        for (int k=0; k<answer.size(); k++) {
            ret[k] = answer.get(k);
        }
        
        return ret;
    }
}