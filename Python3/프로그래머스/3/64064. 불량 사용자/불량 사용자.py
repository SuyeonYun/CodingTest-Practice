import copy

def solution(user_id, banned_id):
    u_dict = {}
    b_dict = {}
    u_idx = 1
    for user in user_id:
        u_dict[user] = u_idx
        u_idx += 1
    
    b_idx = 0
    for ban in banned_id:
        b_idx += 1
        b_dict[b_idx] = []
        for user in user_id:
            if len(user) == len(ban):
                TF = True
                for i in range(len(user)):
                    if ban[i] == '*':
                        continue
                    if user[i] != ban[i]:
                        TF = False
                        break
                if TF:
                    b_dict[b_idx].append(u_dict[user])
    
    answer_set = set()          
    def comb(idx, s):
        nonlocal answer_set
        for u in b_dict[idx]:
            temp = copy.deepcopy(s)
            temp.add(u)
            if len(temp) == len(s) + 1:
                if idx == b_idx:
                    answer_set.add(frozenset(temp))
                else:
                    comb(idx + 1, temp)
        return
            
    comb(1, set())
    return len(answer_set)
