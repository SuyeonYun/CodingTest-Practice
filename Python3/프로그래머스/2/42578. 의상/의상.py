def solution(clothes):
    dict = {}
    result = 1
    
    for i, j in clothes:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
    
    for i in dict:
        result *= dict[i] + 1

    return result - 1
            