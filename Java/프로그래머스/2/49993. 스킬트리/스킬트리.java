import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        int idx;
        List<Integer> temp;
        List<Integer> s_temp;
        for (String ex : skill_trees) {
            temp = new ArrayList<>();
            for (int i=0; i<skill.length(); i++) {
                idx = ex.indexOf(skill.charAt(i));
                temp.add(idx == -1 ? Integer.MAX_VALUE : idx);
            }
            s_temp = new ArrayList<>(temp);
            Collections.sort(s_temp);
            
            if (temp.equals(s_temp)) answer ++;
        }
        return answer;
    }
}