def solution(participant, completion):
    part_dict = {}
    for i in range(len(participant)):
        part_dict[participant[i]] = (part_dict.get(participant[i]) or 0) + 1
        
        if i < len(completion):
            part_dict[completion[i]] = (part_dict.get(completion[i]) or 0) - 1
    
    for ret in part_dict.keys():
        if part_dict[ret] > 0:
            return ret