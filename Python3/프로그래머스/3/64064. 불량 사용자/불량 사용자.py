import re

def solution(user_id, banned_id):
    user_dict = {}
    idx = 0
    for user in user_id:
        user_dict[user] = idx
        idx += 1
    
    candidate = [[] * l for l in range(len(banned_id))]
    for i in range(len(banned_id)):
        bid = banned_id[i]
        for uid in user_id:
            if re.fullmatch(re.sub(r'\*', '[a-z0-9]', bid), uid):
                candidate[i].append(user_dict[uid])
    
    answer_set = set()
    def comb(depth, idx, t_set):
        t_set.add(candidate[depth][idx])
        
        if len(t_set) == depth + 1:
            if depth == len(candidate) - 1:
                answer_set.add(frozenset(t_set))
            else:
                for i in range(len(candidate[depth + 1])):
                    comb(depth + 1, i, set(t_set))   
        else:
            return
            
    for i in range(len(candidate[0])):
        comb(0, i, set())

    return(len(answer_set))
