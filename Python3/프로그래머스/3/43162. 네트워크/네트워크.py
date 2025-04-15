def solution(n, computers):
    total = [i for i in range(n)]
    queue = []
    answer = 0
    
    while(total):
        answer += 1
        queue.append(total.pop(0))
        while(queue):
            cur = queue.pop(0)
            for i in range(n):
                if i != cur and computers[cur][i] == 1 and i in total:
                    queue.append(i)
                    total.remove(i)
                    computers[cur][i] = 0
                    computers[i][cur] = 0
    return answer
