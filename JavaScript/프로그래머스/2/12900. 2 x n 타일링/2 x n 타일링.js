function solution(n) {
    const mod = 1_000_000_007;
    var dp = [];
    
    dp.push(1);
    dp.push(2);
    
    for (let i=2; i<n; i++) {
        let temp = (dp[i - 1] + dp[i - 2]);
        if (temp >= mod) temp = temp % mod;
        dp.push(temp);
    }
    return dp[n - 1];
}