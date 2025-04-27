import re

def solution(s):
    arr = []
    answer = []
    
    s = s[2 : -2].split("},{")
    for str in s:
        str = list(map(int, str.split(',')))
        arr.append(str)
    arr.sort(key = lambda obj: len(obj))
    
    for tup in arr:
        for val in tup:
            if val not in answer:
                answer.append(val)
                break
                
    return answer