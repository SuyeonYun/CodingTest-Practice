from itertools import permutations as per

def solution(k, dungeons):
    max_cnt = 0
    
    for order in per(dungeons, len(dungeons)):
        cnt = 0
        cur_k = k
        
        for st, need in order:
            if cur_k >= st:
                cnt += 1
                cur_k -= need  
                
        max_cnt = max(max_cnt, cnt)
        
    return max_cnt