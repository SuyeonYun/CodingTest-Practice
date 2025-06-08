def solution(stones, k):
    answer = 0
    prev_num = 0
    l = len(stones)
    prev = [i for i in range(-1, l - 1)]
    nextt = [j for j in range(1, l + 1)]
    
    for i in sorted(range(l), key = lambda x: stones[x]):
        if prev[i] > -1:
            nextt[prev[i]] = nextt[i]
        if nextt[i] < l:
            prev[nextt[i]] = prev[i]
        answer += stones[i] - prev_num
        prev_num = stones[i]
        if nextt[i] - prev[i] > k:
            break
    
    return answer
