def solution(sticker):
    l = len(sticker)
    
    if l < 3:
        return max(sticker)
    
    dp1 = []
    dp1.append(sticker[0])
    dp1.append(sticker[0])
    for i in range(2, l - 1):
        dp1.append(max(dp1[i - 2] + sticker[i], dp1[i - 1]))
    dp1.append(dp1[-1])
    
    dp2 = []
    dp2.append(0)
    dp2.append(sticker[1])
    for j in range(2, l):
        dp2.append(max(dp2[j - 2] + sticker[j], dp2[j - 1]))
        
    max1 = max(dp1)
    max2 = max(dp2)
    answer = max(max1, max2)
        
    return answer