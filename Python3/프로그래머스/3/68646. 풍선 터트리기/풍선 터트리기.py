def solution(a):
    cnt = 0
    l = len(a)
    answer = l
    past_idxs = []
    for i in sorted(range(l), key = lambda x : a[x]):
        cnt += 1
        if cnt < 3:
            past_idxs.append(i)
            min_idx = min(past_idxs)
            max_idx = max(past_idxs)
        else:
            if min_idx < i < max_idx:
                answer -= 1
                continue
            if min_idx > i:
                min_idx = i
            if max_idx < i:
                max_idx = i
                
    return answer
            