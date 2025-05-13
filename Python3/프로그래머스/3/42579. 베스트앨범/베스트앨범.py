def solution(genres, plays):
    answer = []
    g_order = []
    g_dict = {}
    
    for i in range(len(genres)):
        if genres[i] in g_dict:
            g_dict[genres[i]].append([i, plays[i]])
        else:
            g_order.append(genres[i])
            g_dict[genres[i]] = [[i, plays[i]]]
    
    g_order.sort(key = lambda x : sum(y[1] for y in g_dict[x]), reverse = True)
    for key in g_dict.keys():
        g_dict[key].sort(key = lambda x : x[1], reverse = True)
    
    for genre in g_order:
        answer.append(g_dict[genre][0][0])
        if len(g_dict[genre]) >= 2:
            answer.append(g_dict[genre][1][0])
    
    return answer
