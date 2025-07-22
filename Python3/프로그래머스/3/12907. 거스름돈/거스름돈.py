def solution(n, money):
    l = len(money)
    money.sort()
    
    for i in range(l):
        if money[i] > n:
            l = i
            break
            
    dp = []    
    cur = money[0]
    max_num = 1_000_000_007
    for i in range(1, n + 1):
        if i % cur == 0:        
            dp.append(1)
        else:
            dp.append(0)
        
    for i in range(1, l):
        cur = money[i]
        dp[cur - 1] += 1
        for j in range(cur, n):
            dp[j] += dp[j - cur]
            if dp[j] > max_num:
                dp[j] %= max_num
            
    return dp[-1]
    