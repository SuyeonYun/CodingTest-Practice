def solution(brown, yellow):
    plus = int((brown + 4) / 2)
    mul = brown + yellow
    
    for x in range(1, plus):
        y = plus - x
        if x * y == mul:
            return [y, x]