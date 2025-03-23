def solution(s):
    answer = []
    pdict = {}
    for i in range(len(s)):
        if s[i] in pdict:
            answer.append(i - pdict[s[i]])
        else:
            answer.append(-1)
        pdict[s[i]] = i
    return answer