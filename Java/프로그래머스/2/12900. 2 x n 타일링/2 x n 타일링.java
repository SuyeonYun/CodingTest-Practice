import java.util.*;

class Solution {
    public int solution(int n) {
        int temp;
        int mod =  1_000_000_007;
        int[] dp = new int[n+2];
        
        dp[0] = 1;
        dp[1] = 2;
        
        for (int i=2; i<n; i++) {
            temp = dp[i - 2] + dp[i - 1];
            dp[i] = temp >= mod ? temp % mod : temp;
        }
        return (dp[n - 1]);
    }
}