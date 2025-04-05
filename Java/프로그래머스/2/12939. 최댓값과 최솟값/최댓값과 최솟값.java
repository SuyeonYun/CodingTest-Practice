import java.util.*;

class Solution {
    public String solution(String s) {
        String[] str = s.split(" ");
        Integer[] arr = new Integer[str.length];
        for (int i=0; i<str.length; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }
        Arrays.sort(arr);
        return String.format("%d %d", arr[0], arr[arr.length - 1]);
    }
}