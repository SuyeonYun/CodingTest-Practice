def solution(s):
    temp = [int(x) for x in s.split(" ")]
    temp.sort()
    return f"{temp[0]} {temp[-1]}"