def solution(ingredient):
    corr = [1,2,3,1]
    count = 0
    stack = []
    for ing in ingredient:
        stack.append(ing)
        if stack[-4:] == corr:
            count += 1
            for i in range(4):
                stack.pop()
    return count