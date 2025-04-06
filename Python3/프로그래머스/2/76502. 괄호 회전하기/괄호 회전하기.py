def is_right(str):
    stack = []
    for s in str:
        if len(stack) != 0:
            if (s == ")" and stack[-1] == "(") or (s == "}" and stack[-1] == "{") or (s == "]" and stack[-1] == "["): 
                stack.pop()
                continue
        stack.append(s)
    if len(stack) == 0: 
        return True
    return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        if is_right(s[i:] + s[:i]): 
            answer += 1
    return answer