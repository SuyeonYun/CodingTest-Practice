from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append((begin, 0))
    
    if target not in words:
        return 0
    
    while len(q) != 0:
        cur, depth = q.popleft()
        if cur == target:
            return depth
        for word in words:
            t_cnt = 0
            for i in range(len(word)):
                if cur[i] != word[i]:
                    t_cnt += 1
            if t_cnt == 1:
                q.append((word, depth + 1))
    return 0
