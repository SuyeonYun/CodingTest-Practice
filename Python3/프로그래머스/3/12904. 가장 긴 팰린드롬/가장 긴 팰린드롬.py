def solution(s):
    p, r = -1, -1
    temp = '#'
    for i in range(len(s)):
        temp += f'{s[i]}#'
        
    s = temp
    l = len(s)
    dp = [0 for _ in range(l)]
    
    for i in range(l):
        if i > r:
            p = i
            r = i
            while r < l and 2 * p - r >= 0 and s[r] == s[2 * p  - r]:
                r += 1
            r -= 1
            dp[i] = r - p

        else:
            j = 2 * p - i
            if dp[j] < r - i:
                dp[i] = dp[j]
            elif dp[j] > r - i:
                dp[i] = r - i
            else:
                p = i
                while r < l and 2 * p - r >= 0 and s[r] == s[2 * p  - r]:
                    r += 1
                r -= 1
                dp[i] = r - p            

    #print(dp)                
    return max(dp)
