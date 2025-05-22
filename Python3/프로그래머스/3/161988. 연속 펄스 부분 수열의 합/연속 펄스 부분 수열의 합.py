import numpy as np
def solution(sequence):
    pulse = np.array([1 if i%2==0 else -1 for i in range(len(sequence))])

    seq = pulse*sequence

    dp = seq.cumsum()

    mx = np.max(dp) - min(np.min(dp), 0)
    mn = abs(np.min(dp) - max(np.max(dp), 0))

    return int(max(mx, mn)) 