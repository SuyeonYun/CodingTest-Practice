def solution(friends, gifts):
    n = len(friends)
    index_dict = {}
    result = [0 for _ in range(n)]
    person_table = [0 for _ in range(n)]
    pair_table = [[0 for _ in range(n)] for _ in range(n)]
    
    idx = 0
    for i in friends:
        index_dict[i] = idx
        idx += 1
    
    for i in gifts:
        f, t = i.split(" ")
        
        i_f = index_dict[f]
        i_t = index_dict[t]
        
        person_table[i_f] += 1
        person_table[i_t] -= 1
        
        pair_table[i_f][i_t] += 1
        
    for i in range(n):
        for j in range(i+1, n):
            idx_i = index_dict[friends[i]]
            idx_j = index_dict[friends[j]]
            
            if pair_table[idx_i][idx_j] > pair_table[idx_j][idx_i]:
                result[idx_i] += 1
            elif pair_table[idx_i][idx_j] < pair_table[idx_j][idx_i]:
                result[idx_j] += 1
            else:
                if person_table[idx_i] > person_table[idx_j]:
                    result[idx_i] += 1
                elif person_table[idx_i] < person_table[idx_j]:
                    result[idx_j] += 1
                    
    return max(result)

        
    