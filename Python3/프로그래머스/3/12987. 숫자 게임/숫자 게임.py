def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    
    idx_a, idx_b, count = 0, 0, 0
    while idx_a < len(A):
        if B[idx_b] > A[idx_a]:
            count += 1
            idx_b += 1
        idx_a += 1

    return count
