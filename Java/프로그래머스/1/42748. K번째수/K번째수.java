import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int[] temp, com;
        int i,j,k;
        
        for(int m=0; m<commands.length; m++) {
            com = commands[m];
            i = com[0] - 1;
            j = com[1];
            k = com[2] - 1;
            
            temp = Arrays.copyOfRange(array, i, j);
            Arrays.sort(temp);
            answer[m] = temp[k];
        }
        
        return answer;
    }
}