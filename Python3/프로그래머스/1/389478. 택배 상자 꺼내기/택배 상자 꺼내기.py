def solution(n, w, num):
    min_h = n // w
    max_h = min_h + 1
    count_min = max_h * w - n

    cur_h = (num - 1) // w

    if cur_h % 2 == 0:
        cur_w = (num - 1) % w
    else:
        cur_w = w * (cur_h + 1) - num

    min_idx = []
    for i in range(count_min):
        if max_h % 2 == 0:
            min_idx.append(i)
        else:
            min_idx.append(w - i - 1)

    if cur_w in min_idx:
        return min_h - cur_h
    return max_h - cur_h