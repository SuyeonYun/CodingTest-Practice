def solution(strings, n):
    strings.sort()
    strings.sort(key = lambda s: s[n])
    return strings