import java.util.*;

class Solution {
    public String solution(String s) {
        String[] arr = Arrays.stream(s.split(" ", -1))
            .map(str -> str.length() >= 1 
                ? String.format("%c%s",
                    Character.toUpperCase(str.charAt(0)),
                    str.substring(1).toLowerCase())
                : str)
            .toArray(String[]::new);
        
        return String.join(" ", arr);
    }
}