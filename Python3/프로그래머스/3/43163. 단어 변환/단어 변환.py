def solution(begin, target, words):
    depth = 0
    cur = begin
    queue = [[cur, 0]]
    
    if target not in words:
        return 0
    
    while queue:        
        cur = queue.pop(0)

        depth = cur[1] + 1
        for word in words:
            cnt = 0
            for i in range(len(target)):
                if word[i] != cur[0][i]:
                    cnt += 1
            if cnt == 1:
                if word == target:
                    return depth
                queue.append([word, depth])
    return 0
