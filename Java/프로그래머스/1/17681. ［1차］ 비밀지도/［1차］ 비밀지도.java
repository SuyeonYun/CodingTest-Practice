import java.util.*;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];

        for (int i = 0; i < n; i++) {
            int combined = arr1[i] | arr2[i];
            
            answer[i] = "";

            String binary = Integer.toBinaryString(combined);
            while (binary.length() < n) {
                binary = "0" + binary;
            }

            for (int j = 0; j < binary.length(); j++) {
                answer[i] += (binary.charAt(j) == '1' ? '#' : ' ');
            }
        }

        return answer;
    }
}
