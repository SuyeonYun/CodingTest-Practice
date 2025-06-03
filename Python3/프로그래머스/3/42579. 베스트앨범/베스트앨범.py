import heapq

def solution(genres, plays):
    answer = []
    g_queue = []
    g_dict = {}
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        if g in g_dict:
            for j in range(len(g_queue)):
                if g_queue[j][1] == g:
                    g_queue[j][0] -= p
        else:
            g_dict[g] = []
            g_queue.append([-p, g])
        heapq.heappush(g_dict[g], (-p, i))
        
    g_queue.sort(key = lambda x: x[0])
            
    for i in range(len(g_queue)):
        genre = g_queue[i][1]
        l = 2
        if len(g_dict[genre]) < 2:
            l = len(g_dict[genre])
        for j in range(l):
            answer.append(heapq.heappop(g_dict[genre])[1])
            
    return answer
