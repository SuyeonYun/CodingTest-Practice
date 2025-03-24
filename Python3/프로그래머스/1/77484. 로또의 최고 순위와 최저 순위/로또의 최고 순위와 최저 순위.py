def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    
    cnt_w = 0
    cnt_z = 0
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt_w += 1
        if lottos[i] == 0:
            cnt_z += 1
    
    answer.append(rank[cnt_w+cnt_z])
    answer.append(rank[cnt_w])
    return answer