def solution(sizes):
    for size in sizes:
        size.sort()
    
    max_w, max_h = sizes[0]
    for i, j in sizes:
        if i > max_w:
            max_w = i
        if j > max_h:
            max_h = j
            
    return max_w * max_h