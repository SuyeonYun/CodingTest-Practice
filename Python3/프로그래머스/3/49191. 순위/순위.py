from collections import deque

def solution(n, results):
    rank = {}
    player = {}
    answer = []
    
    if n < 3:
        return n
    
    for i in range(1, n + 1):
        rank[i] = []
        player[i] = []
    
    result = [[[], []] for _ in range(n + 1)]
    for i in range(len(results)):
        result[results[i][0]][0].append(results[i][1])
        result[results[i][1]][1].append(results[i][0])
    
    for i in range(1, n +1):
        for a in result[i][0]:
            for b in result[a][0]:
                if b not in result[i][0]:
                    result[i][0].append(b)
        for c in result[i][1]:
            for d in result[c][1]:
                if d not in result[i][1]:
                    result[i][1].append(d)
    
    for i in range(1, n + 1):
        w, l = result[i]
        w = len(w)
        l = len(l)
        for j in range(l + 1, n - w + 1):
            player[i].append(j)
            rank[j].append(i)
    
    q = deque()
    for i in range(1, n + 1):
        if len(player[i]) == 1:
            q.append((i, player[i][0]))
        if len(rank[i]) == 1:
            q.append((rank[i][0], i))
    
    while q:
        p, r = q.popleft()
        if p in answer:
            continue
        answer.append(p)
        player[p] = []
        rank[r] = []
        for i in range(1, n + 1):
            if r in player[i]:
                player[i].remove(r)
                if len(player[i]) == 1:
                    q.append((i, player[i][0]))
                
            if p in rank[i]:
                rank[i].remove(p)
                if len(rank[i]) == 1:
                    q.append((rank[i][0], i))
    
    return len(answer)
        