def solution(sticker):
    answer = 0
    n = len(sticker)

    if n <= 3:
        return max(sticker)
    
    dp1 = []
    dp1.append(sticker[0])
    dp1.append(sticker[0])
    for i in range(2, n - 1):
        dp1.append(max(dp1[i - 2] + sticker[i], dp1[i - 1]))
    
    dp2 = []
    dp2.append(0)
    dp2.append(sticker[1])
    for i in range(2, n):
        dp2.append(max(dp2[i - 2] + sticker[i], dp2[i - 1]))

    answer = max(dp1[-1], dp2[-1])
    return answer
